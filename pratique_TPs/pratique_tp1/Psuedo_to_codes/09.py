'''
nombre_secret <- 7
tentative <- 0

tant que tentative != nombre_secret faire:
    tentative <- demander("Devinez le nombre : ")
    si tentative > nombre_secret alors:
        afficher("Trop grand !")
    sinon:
        si tentative < nombre_secret alors:
            afficher("Trop petit !")
        fin si
    fin si
fin tant que

afficher("Bravo ! Vous avez trouvé !")
'''

nombre_secret = 7
tentative = 0

while tentative != nombre_secret:
    tentative = int(input("Devinez le nombre : "))
    if tentative > nombre_secret:
        print("Trop grand !")
    else:
        if tentative < nombre_secret:
            print("Trop petit !")
            
print("Bravo ! Vous avez trouvé !")