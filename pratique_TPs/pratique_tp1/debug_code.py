# Programme pour calculer la moyenne de notes
print("=== Calculateur de moyenne ===")  # `print` non `Print`

# Demander le nom de l'étudiant
nom = input("Nom de l'étudiant : ")

# Initialiser les variables
somme = 0
nb_notes = 5  # initialisation nb_notes = 5 et non verification

# Saisir les notes
for i in range(1, nb_notes):
    note = input(f"Note {i} sur 20 : ")
    somme = somme + note

# Calculer la moyenne
moyenne = somme / nb_notes
print("Bonjour", nom, "votre moyenne est :", moyenne)

# Afficher l'appréciation
if moyenne >= 16: # `:`
    print("Excellent !")
elif moyenne >= 14:
    print("Très bien")
elif moyenne >= 12:
    print("Bien")
elif moyenne >= 10: # elif et non elseif et aussi `:`
    print("Passable")
else:
    print("Insuffisant")

# Vérifier si l'étudiant passe
if moyenne >= 10:
    print("Vous validez l'examen !")
else:
    print("Vous devez repasser l'examen.")
