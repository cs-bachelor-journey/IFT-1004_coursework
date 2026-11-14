# La factorielle d’un nombre n, nommée n!, est définie par le produit 1 · 2 · 3 · . . . · n
# Idée : La factorielle d’un nombre n est le produit entre n et la factorielle du nombre n − 1.

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n -1)