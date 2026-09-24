# Module 01 Quiz

> 1. Donnez les valeurs des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- 8 b <- -a c <- a + b
```

| variable | value |
| -------- | ----- |
| a        | 8     |
| b        | -8    |
| c        | 0     |

---

> 2. Donnez les valeurs des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- 5 b <- 10 + 2 c <- a + b - 3 b <- a
```

| variable | value |
| -------- | ----- |
| a        | 5     |
| b        | 5     |
| c        | 14    |

---

> 3. Donnez les valeurs des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- 1 b <- a a <- a + a a <- a * a * a c <- a + b
```

| variable | value |
| -------- | ----- |
| a        | 8     |
| b        | 1     |
| c        | 9     |

---

> 4. Donnez les types des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- "programmation" b <- 3.0 c <- 3
```

| variable | type                 |
| -------- | -------------------- |
| a        | chaine de caracteres |
| b        | reel                 |
| c        | entier               |

---

> 5. Donnez les types des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- 3.1416 b <- 2 c <- a * b
```

| variable | type   |
| -------- | ------ |
| a        | reel   |
| b        | entier |
| c        | reel   |

---

> 6. Donnez les types des variables a, b et c après l'exécution du pseudo-code suivant:

```text
a <- 3.0 b <- 2 c <- a + b
```

| variable | type   |
| -------- | ------ |
| a        | reel   |
| b        | entier |
| c        | reel   |

---

> 7. Soit la fonction mathématique y = 2x+1, où x et y sont réels. Remplissez ce programme trouvant le y associé à un x en remplaçant la ligne # par votre code:

```bash
x <- demander("x: ") # afficher("y =", y)
```

Answer:

```bash
x <- demander("x: ")

y <- (2*x) + 1

afficher("y =", y)
```

---

> 8. Soit la fonction mathématique y = 2x+1, où x et y sont réels. Remplissez ce programme trouvant le x associé à un y en remplaçant la ligne # par votre code:

```bash
y <- demander("y: ") # afficher("x =", x)
```

Answer:

```bash
y <- demander("y: ")
x <- (y - 1) / 2

afficher("x =", x)

```

---

> 9. Remplissez ce programme trouvant la somme de deux nombres en remplaçant la ligne # par votre code:

```bash
nombre_1 <- demander("Un premier nombre: ")
nombre_2 <- demander("Un deuxième nombre: ")

# afficher("Le somme est:", somme)

```

Answer:

```bash
nombre_1 <- demander("Un premier nombre: ")
nombre_2 <- demander("Un deuxième nombre: ")

somme <- nombre_1 + nombre_2
afficher("Le somme est:", somme)
```

---

> 10. Quel entier obtiendra-t-on suite à l'évaluation de cette expression?

```text
-(3 + 4) - 4 // 2 + 2 * (4) - (-3 + 1)
```

Answer: **1**
solution:

```text
-(3 + 4) - 4 // 2 + 2 * (4) - (-3 + 1)

-7 - 4 // 2 + 2 * (4) - (-2)

-7 (- 4 // 2) + (2 * (4)) - (-2)

-7 - 2 + 8 + 2

(-7 - 2) + 8 + 2

-9 + 8 + 2

-9 + (8 + 2)

-9 + 10

1

```

---

> 11. Quel booléen obtiendra-t-on suite à l'évaluation de cette expression?

```text
(Vrai et Faux) ou Vrai
```

Answer: **Vrai**

---

> 12. Quel booléen obtiendra-t-on suite à l'évaluation de cette expression contenant des entiers?

```text
(3 > 2) et (4 + 5 * 2 == 18)
```

Answer: **Faux**
Solution:

```text
(3 > 2) et (4 + 5 * 2 == 18)

vrai et ( 14 == 18)
vrai et Faux
Faux
```

---

> 13. Quel réel obtiendra-t-on suite à l'évaluation de cette expression?

```text
3.5 * 2 + 8 // 3 + 7.0 / (-1 - 1.0)
```

Answer: **5.5**
Solution:

```text
3.5 * 2 + 8 // 3 + 7.0 / (-1 - 1.0)

3.5 * 2 + 8 // 3 + 7.0 / -2.0

3.5 * 2 +( 8 // 3 )+ (7.0 / -2.0)

3.5 * 2 + 2 + (-3.5)

(3.5 * 2) + 2 -3.5

7.0 + 2 - 3.5

9.0 - 3.5

5.5
```

> 14. Quel booléen obtiendra-t-on suite à l'évaluation de cette expression?

```text
neg (Faux ou Faux) ou neg (Vrai et Vrai)
```

Solution:

```text
neg (Faux ou Faux) ou neg (Vrai et Vrai)

neg (Faux) ou neg (Vrai)

Vrai ou Faux

Vrai
```

---

> 15. Quel booléen obtiendra-t-on suite à l'évaluation de cette expression contenant des entiers?

```text
neg (3 > 2 et Vrai) ou 4 == 12 // 4
```

Solution:

```text
neg (3 > 2 et Vrai) ou 4 == 12 // 4

neg (Vrai et Vrai) ou 4 == 12 // 4

neg (Vrai) ou 4 == 12 // 4

neg (Vrai) ou 4 == (12 // 4)

neg (Vrai) ou 4 == 3

neg (Vrai) ou (4 == 3)

neg (Vrai) ou Faux

(neg (Vrai)) ou Faux

Faux ou Faux

Faux
```

---

> 16. Remplissez ce programme trouvant le maximum entre deux nombres en remplaçant la ligne # par votre code (utiliser l'instruction si!):

```text
nombre_1 <- demander("Un premier nombre: ") nombre_2 <- demander("Un deuxième nombre: ") # afficher("Le plus grand nombre est:", plus_grand_nombre)
```

Solution:

```bash
nombre_1 <- demander("Un premier nombre: ")
nombre_2 <- demander("Un deuxième nombre: ")

si nombre_1 > nombre_2 alors:
    plus_grand_nombre <- nombre_1
sinon:
    plus_grand_nombre  <- nombre_2

afficher("Le plus grand nombre est:", plus_grand_nombre)
```

---

> 17. Quel entier donné en entrée résulterait en l'affichage du "Bravo!" ?

```text
x <- demander("Tentez de deviner l'entier secret: ") si neg (x <= 10 ou x >= 15) alors: si x % 3 == 1 alors: afficher("Bravo!") fin si fin si
```

Solution:

```bash
x <- demander("Tentez de deviner l'entier secret: ")

si neg (x <= 10 ou x >= 15) alors:
    si x % 3 == 1 alors:
        afficher("Bravo!")
    fin si
fin si

x must lesthan 10 or greater than 15 to be true.

(x <= 10 ou x >= 15)  must be False

if  x = 13

neg ( 13 <= 10 ou 13 >= 15)

neg( Faux ou Faux)

neg(Faux)

Vrai

x % 3 == 1 must be true

13 % 3 == 1

Vrai

l'entier secret: 13
```

---

> 18. Quel entier donné en entrée résulterait en l'affichage du "Bravo!" ?

```bash
x <- demander("Tentez de deviner l'entier secret: ")
y <- x * 2

si x % 3 == 0 alors:
    y <- y * 2
fin si

si x > 5 et y < 15 alors:
    afficher("Bravo!")
fin si

```

Solution:

```text
x must be greater than 5 and must not be divisible by 3

y <- x * 2 must be less than 15

l'entier secret: 7
```

---

> 19. Donnez l'affichage de l'algorithme suivant:

```bash
x <- 0

si x >= 12 alors: # 0 >= 12 False
    si x == 0 alors:
        x <- 12
    sinon:
        x <- 24
    fin si
sinon:
    si x <= 12 alors: # 0 <= 12 True
        x <- 36 # x = 36
    sinon:
        x <- 48
    fin si
fin si

afficher(x // 12) # 36 // 12 = 3

```

Answer: **3**

---

> 20. Donnez l'affichage de l'algorithme suivant:

```bash
x <- 0 # 0 1 2 3 4 5 6 7 8 9 10 11
somme <- 0 # 0 0 1 3 6 10 15 21 28 36 45 55

tant que x <= 10 faire: # 0 1 2 3 4 5 6 7 8 9 10 11 -> Faux
    somme <- somme + x # 0 1 3 6 10 15 21 28 36 45 55
    x <- x + 1 # 1 2 3 4 5 6 7 8 9 10 11
fin tant que

afficher(somme) # 55

```

---

> 21. À l'aide d'une boucle tant que, écrivez un algorithme qui calcule la somme de tous les nombres plus petits ou égaux à un nombre fourni en entrée en remplaçant la ligne # par votre code.

```text
x <- demander("Entier fourni: ") # afficher(somme)
```

Solution:

```bash
x <- demander("Entier fourni: ")

# 5  => 1 + 2 + 3  + 4 + 5 = 15

somme <- 0 # 5
i <- x. # 5 4

tant que  i >= 0   faire:
    somme <- somme + i # 5
    i <- i - 1 # 4

fin tant que

afficher(somme)
```

---

> 22. Réécrivez votre algorithme de la question précédente avec une boucle pour tout.

```bash
x <- demander("Entier fourni: ")

somme <- 0

pour tout num dans < 1, 2 , ... n> faire:
    somme <- somme + num

fin pour

afficher(somme)

```
