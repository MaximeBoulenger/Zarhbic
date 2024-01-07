"""
    Modules:
    - sys : Accéder à certaines fonctionnalités spécifiques du système d'exploitation.
    - deque : Importer la classe deque pour utiliser des files.
    - sympify : Calculer le résultat final de façon sécurisé
"""
import sys
from collections import deque
from sympy import sympify


class Zarhbic:
    """
    Classe Zarhbic pour traiter des expressions mathématiques simplifiées.

    Attributes:
    - expression_complete (str): L'expression mathématique complète après traitement.
    - expression (str): L'expression mathématique d'origine sous forme de chaîne de caractères.
    - expressionListe (list): Une liste des caractères de l'expression sans espaces.
    - chiffres (collections.deque): Une file pour stocker les chiffres extraits de l'expression.
    - operateurs (collections.deque): Une file pour stocker les opérateurs extraits de l'expression.
    - nombre_en_cours (str): Variable temporaire pour construire les nombres pendant le traitement.
    """

    def __init__(self, expression):
        """
        Initialise une instance de la classe Zarhbic.

        Parameters:
        - expression (str): L'expression mathématique sous forme de chaîne de caractères.
        """
        self.expression_complete = None
        self.expression = expression
        self.expressionListe = list(expression)
        self.chiffres = deque()
        self.operateurs = deque()
        self.nombre_en_cours = ""

    def saisir_expression(self):
        """
        Demande à l'utilisateur une expression mathématique.
        """
        self.expression = input("Entrez une chaîne de caractères contenant des chiffres et des"
                                " opérateurs : ")
        self.expressionListe = list(self.expression)
        while " " in self.expressionListe:
            self.expressionListe.remove(" ")

    def traiter_expression(self):
        """
        Traite l'expression en extrayant les chiffres et les opérateurs pour les stocker
        dans les attributs correspondants.
        """
        for caractere in self.expression:
            if caractere.isdigit():
                self.nombre_en_cours += caractere
            elif caractere == " " and self.nombre_en_cours:
                self.chiffres.appendleft(int(self.nombre_en_cours))
                self.nombre_en_cours = ""
            elif caractere in ['+', '-', '*', '/']:
                self.operateurs.appendleft(caractere)

        if self.nombre_en_cours:
            self.chiffres.appendleft(int(self.nombre_en_cours))

    def afficher_resultat(self):
        """
        Affiche les chiffres et opérateurs traités.
        """
        print("Chiffres traités:", " ".join(map(str, self.chiffres)))
        print("Opérateurs traités:", " ".join(self.operateurs))

    def verifier_calcul(self):
        """
        Vérifie si l'expression a été correctement saisie.
        """
        if len(self.chiffres) >= 2 and len(self.operateurs) == len(self.chiffres) - 1:
            print("Le calcul a été correctement entré.")
        else:
            print("Erreur, le calcul a mal été saisi.")
            sys.exit()

    def inverser_files(self):
        """
        Inverse les opérateurs ou les opérandes dans certains cas spécifiques.
        """
        if (len(self.operateurs) >= 2 and self.expressionListe[-1] == '-' and
                self.expressionListe[-2] in ['+', '-', '*', '/']):
            print("Inversion des opérateurs")
            self.operateurs.reverse()
        elif (len(self.operateurs) >= 2 and self.expressionListe[-1] == '*' and
              self.expressionListe[-2] in ['+', '-', '*', '/']):
            print("Inversion des chiffres")
            self.chiffres.reverse()

    def construire_expression_complete(self):
        """
        Construit l'expression complète à partir des chiffres et opérateurs traités.
        """
        if len(self.operateurs) == 1:
            self.expression_complete = f"{self.chiffres[1]} {self.operateurs[0]} {self.chiffres[0]}"
        elif self.operateurs[0] == '+':
            self.expression_complete = (f"{self.chiffres[2]} {self.operateurs[1]}"
                                        f" ({self.chiffres[1]} {self.operateurs[0]}"
                                        f" {self.chiffres[0]})")
        elif self.operateurs[1] == '+':
            self.expression_complete = (f"({self.chiffres[2]} {self.operateurs[1]}"
                                        f" {self.chiffres[1]}) {self.operateurs[0]}"
                                        f" {self.chiffres[0]}")
        else:
            self.expression_complete = (f"{self.chiffres[2]} {self.operateurs[1]} "
                                        f"{self.chiffres[1]} {self.operateurs[0]}"
                                        f" {self.chiffres[0]}")

    def afficher_resultat_final(self):
        """
        Affiche l'expression complète et le résultat final du calcul.
        """
        print(self.expression_complete)
        print("Résultat final :", sympify(self.expression_complete))


def main():
    """
    Fonction principale du programme. Crée une instance de Zarhbic, saisit l'expression,
    traite l'expression, effectue des opérations et affiche le résultat final.
    """
    zarhbic = Zarhbic("")
    zarhbic.saisir_expression()
    zarhbic.traiter_expression()
    zarhbic.afficher_resultat()
    zarhbic.verifier_calcul()
    zarhbic.inverser_files()
    zarhbic.construire_expression_complete()
    zarhbic.afficher_resultat_final()


if __name__ == "__main__":
    main()
