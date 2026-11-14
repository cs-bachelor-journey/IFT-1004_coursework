def hanoi(n, source , auxiliaire , destination ):
    if n == 1:
        print(f"Déplacer {source} vers {destination}")
    else:
        hanoi(n - 1, source , destination , auxiliaire)
        print(f"Déplacer {source} vers {destination}")
        hanoi(n - 1, auxiliaire , source , destination)