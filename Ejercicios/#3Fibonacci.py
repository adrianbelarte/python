### 3 LA SUCESIÓN DE FIBONACCI

"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

# x + 1x = x
n = 0
y = 1

for index in range (0,51):
    print(n)
    fib = n + y
    n = y
    y = fib