import sys
from collections import deque


class Zarhbic:
    def __init__(self, expression):
        """
        Initialise une instance de la classe Zarhbic.

        Parameters:
        - expression (str): L'expression mathématique sous forme de chaîne de caractères.
        """
        self.expression_complete = None
        self.expression = expression
        self.expressionListe = list(expression)
        while " " in self.expressionListe:
            self.expressionListe.remove(" ")

        self.chiffres = deque()
        self.operateurs = deque()
        self.nombre_en_cours = ""

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

    def inverser_operateurs(self):
        """
        Inverse les opérateurs dans certains cas spécifiques.
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
        print("Résultat final :", eval(self.expression_complete))


def main():
    """
    Fonction principale du programme. Demande à l'utilisateur une expression mathématique,
    crée une instance de Zarhbic, traite l'expression, effectue des opérations et affiche
    le résultat final.
    """
    expression_utilisateur = input("Entrez une chaîne de caractères contenant des chiffres et des"
                                   " opérateurs : ")

    zarhbic = Zarhbic(expression_utilisateur)
    zarhbic.traiter_expression()
    zarhbic.afficher_resultat()
    zarhbic.verifier_calcul()
    zarhbic.inverser_operateurs()
    zarhbic.construire_expression_complete()
    zarhbic.afficher_resultat_final()


if __name__ == "__main__":
    main()
