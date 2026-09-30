'''
age <- demander("Votre âge : ")

si age >= 18 alors:
    afficher("Vous êtes majeur")
sinon:
    afficher("Vous êtes mineur")
fin si
'''

age = int(input("Votre âge : "))

if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")