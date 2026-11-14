# La suite de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Conditions d’arrêt : f(0) = 0 et f(1) = 1
# Récursion : f(n) = f(n − 1) + f(n − 2)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 2) + fibonacci(n - 1)