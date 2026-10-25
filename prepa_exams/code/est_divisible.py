# Écrivez le code d’un programme Python qui demande à
# l’utilisateur d’entrer des nombres entiers plus grands que zéro, tant et aussi longtemps que
# le nombre entré est divisible par le précédent. Le résultat de l’exécution de votre programme
# doit respecter exactement les deux exemples suivants:
# Premier exemple d’exécution : Deuxième exemple d’exécution :
# Entrez un entier positif: 1
# Entrez un entier positif: 2
# 2 est divisible par 1
# Entrez un entier positif: 88
# 88 est divisible par 2
# Entrez un entier positif: 90
# 90 n'est pas divisible par 88.
# Entrez un entier positif: 1608
# Entrez un entier positif: 2022
# 2022 n'

est_divisible = True
nombre_un = int (input('Entrez un entier positif:'))

while est_divisible:
    nombre_deux = int (input('Entrez un entier positif:'))
    if nombre_deux % nombre_un == 0:
        print(nombre_deux , "est divisible par", nombre_un)
    else :
        print(nombre_deux , "n'est pas divisible par", nombre_un)
        est_divisible = False
        
    nombre_un = nombre_deux