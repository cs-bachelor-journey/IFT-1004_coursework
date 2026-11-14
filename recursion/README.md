# Recursion

Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems.

## Types of Recursion

### Direct Recursion

Direct recursion occurs when a function calls itself directly.

For example:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

## Divide and Conquer

Divide and conquer is a technique where a problem is divided into smaller subproblems, solved independently, and then combined to form the final solution. This often involves recursion.

For example, sum of elements in an array can be solved using divide and conquer:

```python
def sum_array(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_array(arr[1:])
```

## Some Common Examples of Recursion

### Fibonacci

> f(n) = f(n -1) + f(n - 2) for n >= 2, with base cases f(0) = 0 and f(1) = 1.

### Greatest Common Divisor (GCD)

> gcd(a, b) = a if a = b
> gcd(a, b) = gcd(a -b, b) if a > b
> gcd(a, b) = gcd(a, b - a) if a < b
