expression = input("Entrez une chaîne de caractères contenant des chiffres et des opérateurs : ")

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
    print("Erreur, le nombre d'opérateur est incorrect!")
    print("Exemple correct : 1+1+1 / Exemple incorrect : 1+1+1+")
    exit(1)

print("Liste des chiffres:", chiffres)
print("Liste des opérateurs:", operateurs)
print("Liste des caractères inconnus:", inconnus)

reformulation = []

for i in range(max(len(chiffres), len(operateurs))):
    if i < len(chiffres):
        reformulation.append(chiffres[i])
    if i < len(operateurs):
        reformulation.append(operateurs[i])

print("Reformulation:", reformulation)

resultat = ''.join(map(str, reformulation))
print("Le résultat est ", eval(resultat))

"""Problème : le calcul numéro 5 ne fonctionne pas"""
