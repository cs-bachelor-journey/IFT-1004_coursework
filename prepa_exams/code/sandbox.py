
# a = -1
# compteur = 0 
# while a >= -1 and a <= 1:
#     a = a + 1
#     compteur += 1
    
# print(compteur) # max value of compteur will 3 when a = -1

# print("=" *20)

print("===========" * 10)

name = "Loko Ismael"

# name[start_index:stop_index - 1] # Note: stop_index is not included
print(name[-1])
print(name[::-1])

# is palindrome

print(f"is_palindrome {name == name[::-1]}")


print("===========" * 10)

def somme(a: int, b: int) -> float:
    """add two numbers

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        float: _description_
    """
    return float(a + b)

print(somme.__doc__)
    