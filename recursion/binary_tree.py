def creer_arbre(donnee ):
    return {'donnee ':donnee , 'gauche ':None , 'droite ':None}

def inserer_arbre(donnee , racine ):
    if racine is None:
        racine = creer_arbre(donnee)
    else:
        if donnee <= racine['donnee ']:
            racine['gauche '] = inserer_arbre(donnee , racine['gauche '])
        else:
            racine['droite '] = inserer_arbre(donnee , racine['droite '])
            
    return racine

arbre = None
for i in [8, 3, 6, 1, 10, 4, 14, 7, 13]:
    arbre = inserer_arbre(i, arbre)