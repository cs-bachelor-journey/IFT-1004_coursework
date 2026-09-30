'''
compteur_pairs <- 0

pour tout i dans <1,2,...,10> faire:
    si i % 2 == 0 alors:
        afficher(i, "est pair")
        compteur_pairs <- compteur_pairs + 1
    fin si
fin pour tout

afficher("Total de nombres pairs :", compteur_pairs)
'''

compteur_pairs = 0

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "est pair")
        compteur_pairs += 1

print("Total de nombres pairs :", compteur_pairs)