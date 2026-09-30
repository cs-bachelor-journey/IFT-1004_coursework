'''
maximum <- 0
pour tout i dans <1,2,3,4,5> faire:
    nombre <- demander("Entrez un nombre : ")
    si nombre > maximum alors:
        maximum <- nombre
    fin si
fin pour tout
afficher("Le maximum est :", maximum)
'''

maximum = 0

for i in range(1, 6):
    nombre = int(input("Entrez in nombre : "))
    
    if nombre > maximum:
        maximum = nombre

print("Le maximum est :", maximum)