'''
nombre <- demander("Table de multiplication de : ")

pour tout i dans <1,2,...,10> faire:
    resultat <- nombre * i
    afficher(nombre, "x", i, "=", resultat)
fin pour tout
'''

nombre = int(input("Table de multiplication de : "))

for i in range(1, 11):
    resultat = nombre * i
    print(nombre, "x", i, "=", resultat)