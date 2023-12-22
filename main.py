from collections import deque


class Zarhbic:
    def __init__(self, expression):
        self.expression_complete = None
        self.expression = expression
        self.expressionListe = list(expression)
        while " " in self.expressionListe:
            self.expressionListe.remove(" ")

        self.chiffres = deque()
        self.operateurs = deque()
        self.nombre_en_cours = ""

    def traiter_expression(self):
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
        print("Chiffres traités:", " ".join(map(str, self.chiffres)))
        print("Opérateurs traités:", " ".join(self.operateurs))

    def verifier_calcul(self):
        if len(self.chiffres) >= 2 and len(self.operateurs) == len(self.chiffres) - 1:
            print("Le calcul a été correctement entré.")
        else:
            print("Erreur, le calcul a mal été saisi.")
            exit(1)

    def inverser_operateurs(self):
        if len(self.operateurs) >= 2 and self.expressionListe[-1] == '-' and self.expressionListe[-2] in ['+', '-', '*',
                                                                                                          '/']:
            print("Inversion des opérateurs")
            self.operateurs.reverse()
        elif len(self.operateurs) >= 2 and self.expressionListe[-1] == '*' and self.expressionListe[-2] in ['+', '-',
                                                                                                            '*', '/']:
            print("Inversion des chiffres")
            self.chiffres.reverse()

    def construire_expression_complete(self):
        if len(self.operateurs) == 1:
            self.expression_complete = f"{self.chiffres[1]} {self.operateurs[0]} {self.chiffres[0]}"
        elif self.operateurs[0] == '+':
            self.expression_complete = (f"{self.chiffres[2]} {self.operateurs[1]} ({self.chiffres[1]}"
                                        f" {self.operateurs[0]} {self.chiffres[0]})")
        elif self.operateurs[1] == '+':
            self.expression_complete = (f"({self.chiffres[2]} {self.operateurs[1]} {self.chiffres[1]})"
                                        f" {self.operateurs[0]} {self.chiffres[0]}")
        else:
            self.expression_complete = (f"{self.chiffres[2]} {self.operateurs[1]} {self.chiffres[1]}"
                                        f" {self.operateurs[0]} {self.chiffres[0]}")

    def afficher_resultat_final(self):
        print(self.expression_complete)
        print("Résultat final :", eval(self.expression_complete))


def main():
    expression_utilisateur = input("Entrez une chaîne de caractères contenant des chiffres et des opérateurs : ")

    zarhbic = Zarhbic(expression_utilisateur)
    zarhbic.traiter_expression()
    zarhbic.afficher_resultat()
    zarhbic.verifier_calcul()
    zarhbic.inverser_operateurs()
    zarhbic.construire_expression_complete()
    zarhbic.afficher_resultat_final()


if __name__ == "__main__":
    main()
