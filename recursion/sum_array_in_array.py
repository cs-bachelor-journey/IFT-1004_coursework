# Supposons que l’on veut récursivement sommer les éléments d’une liste de listes de listes, etc...

une_liste_recursive = [12, [1,2,3], [0, [1,2]]]

def somme(liste):
    resultat = 0
    
    for element in liste:
        if isinstance(element, list): # check type(element) == list
            resultat += somme(element)
        else:
            resultat += element
            
    return resultat