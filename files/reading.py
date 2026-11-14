from os import path 

nom_fichier = input("Veuillez entrer le nom du fichier a lire : ")

if path.isfile(nom_fichier):

    f = open(nom_fichier, "r")

    txt = f.readline()

    while txt != "": # while the end of the file not reached
        
        txt = txt.rstrip("\n")
        
        # sample code
        
        txt = f.readline()

    f.close()
else:
    print("Le fichier", nom_fichier , "est introuvable.")