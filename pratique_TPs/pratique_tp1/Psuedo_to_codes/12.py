'''
afficher("=== MENU ===")
afficher("1. Addition")
afficher("2. Soustraction")
afficher("3. Multiplication")
choix <- demander("Votre choix : ")

si choix == 1 alors:
    a <- demander("Premier nombre : ")
    b <- demander("Deuxième nombre : ")
    afficher("Résultat :", a + b)
sinon:
    si choix == 2 alors:
        a <- demander("Premier nombre : ")
        b <- demander("Deuxième nombre : ")
        afficher("Résultat :", a - b)
    sinon:
        si choix == 3 alors:
            a <- demander("Premier nombre : ")
            b <- demander("Deuxième nombre : ")
            afficher("Résultat :", a * b)
        sinon:
            afficher("Choix invalide")
        fin si
    fin si
fin si
'''

print("=== MENU ===")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")

choix = int(input("Votre choix : "))

if choix == 1:
    a = int(input("Premier nombre : "))
    b = int(input("Deuxième nombre : "))
    
    print("Résultat :", a + b)
else:
    if choix == 2:
        a = int(input("Premier nombre : "))
        b = int(input("Deuxième nombre : "))
    
        print("Résultat :", a - b)
    else:
        if choix == 3:
            a = int(input("Premier nombre : "))
            b = int(input("Deuxième nombre : "))
    
            print("Résultat :", a * b)
        else:
            print("Choix invalide")  