expression = input("Entrez une chaîne de caractères contenant des chiffres et des opérateurs : ")

expressionListe = list(expression)
while " " in expressionListe:
    expressionListe.remove(" ")

chiffres = []
operateurs = []
inconnus = []

nombre_en_cours = ""

for caractere in expression:
    if caractere.isdigit():
        nombre_en_cours += caractere
    elif caractere == " " and nombre_en_cours:
        chiffres.append(int(nombre_en_cours))
        nombre_en_cours = ""
    elif caractere in ['+', '-', '*', '/']:
        operateurs.append(caractere)
    else:
        inconnus.append(caractere)

if nombre_en_cours:
    chiffres.append(int(nombre_en_cours))

if len(chiffres) and len(operateurs) == 0:
    print("Erreur, aucun calcul saisi!")
    exit(1)

if len(chiffres) != len(operateurs) + 1:
    print("Erreur, le nombre d'opérateurs est incorrect!")
    print("Exemple correct : 1+1+1 / Exemple incorrect : 1+1+1+")
    exit(1)

if (len(expressionListe) >= 5 and expressionListe[-1] in operateurs and expressionListe[-2] in
        operateurs):
    print("Exception!")
    if expressionListe[-1] == '*':
        chiffres.reverse()
    else:
        operateurs.reverse()

print("Liste des chiffres:", chiffres)
print("Liste des opérateurs:", operateurs)
print("Liste des caractères inconnus:", inconnus)
print("Liste de l'expression:", expressionListe)

reformulation = []
addition = False

for i in range(len(operateurs)):
    if operateurs[i] == '+':
        reformulation.append('(')
        addition = True
    else:
        addition = False

    if not addition:
        pass
    else:
        reformulation.append(chiffres[i])

    reformulation.append(operateurs[i])

    reformulation.append(chiffres[i + 1])

    if operateurs[i] == '+':
        reformulation.append(')')

print("Reformulation:", reformulation)

resultat = ''.join(map(str, reformulation))
print("Le résultat est", eval(resultat))

"""" Calcul 5 non fonctionnel """
