
# Un palindrome est un mot qui peut être lu de la même manière de gauche à droite ou de droite
# à gauche.

# Idée : Un mot est un palindrome si son premier et son dernier caractères sont les mêmes,
# et si la partie « à l’intérieur » du mot est un palindrome.

def est_palindrome(chaine):
    # conditions 
    if len(chaine) <= 1:
        return True
    
    if chaine[0] != chaine[-1]:
        return False
    
    return est_palindrome(chaine[1:-1])
        
        
## Non recursive form

def est_palindrome_v2(chaine):
    if len(chaine) <= 1:
        return True
    
    for i in range(len(chaine) // 2):
        if chaine[i] != chaine[-i-1]:
            return False 
    
    return True