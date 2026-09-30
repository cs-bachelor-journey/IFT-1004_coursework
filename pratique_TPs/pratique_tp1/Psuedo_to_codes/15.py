'''
n <- demander("Calculer la somme de 1 à : ")
somme <- 0
pour tout i dans <1,2,...,n> faire:
    somme <- somme + i
fin pour tout
afficher("La somme de 1 à", n, "est :", somme)
'''

n = int(input("Calculer la somme de 1 à : "))

somme = 0

for i in range(1, n+1):
    somme += 1

print("La somme de 1 à", n, "est :", somme)
