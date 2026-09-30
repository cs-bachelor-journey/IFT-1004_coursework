'''
somme <- 0

pour tout i dans <1,2,3,4,5> faire:
    note <- demander("Note " + i + " : ")
    somme <- somme + note
fin pour tout

moyenne <- somme / 5
afficher("Moyenne :", moyenne)
'''

somme = 0

for i in range(1, 6):
    note = int(input("Note " + str(i) + " : "))
    somme += note

moyenne = somme/5
print("Moyenne :", moyenne)
