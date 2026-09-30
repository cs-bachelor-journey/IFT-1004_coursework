'''
note <- demander("Votre note sur 20 : ")

si note >= 16 alors:
    afficher("Très bien")
sinon:
    si note >= 14 alors:
        afficher("Bien")
    sinon:
        si note >= 12 alors:
            afficher("Assez bien")
        sinon:
            si note >= 10 alors:
                afficher("Passable")
            sinon:
                afficher("Insuffisant")
            fin si
        fin si
    fin si
fin si
'''

note = float(input("Votre note sur 20 : "))

if note >= 16:
    print("Très bien")
else:
    if note >= 14:
        print("Bien")
    else:
        if note >= 12:
            print("Assez bien")
        else:
            if note >= 10:
                print("Passable")
            else:
                print("Insuffisant")