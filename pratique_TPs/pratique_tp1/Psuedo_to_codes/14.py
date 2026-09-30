'''
age <- 0
tant que age < 1 ou age > 120 faire:
    age <- demander("Votre âge (1-120) : ")
    si age < 1 ou age > 120 alors:
        afficher("Âge invalide, réessayez !")
    fin si
fin tant que
afficher("Votre âge est :", age)
'''

age = 0

while age < 1 or age > 120:
    age = int(input("Votre âge (1-120) : "))
    
    if age < 1 or age > 120:
        print("Âge invalide, réessayez !")
        
print("Votre âge est :", age)