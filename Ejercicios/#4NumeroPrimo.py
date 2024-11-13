### 4 ES UN NÚMERO PRIMO? ###

"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1
 */
"""

def numeroPrimo():
    for number in range(1, 101):

        if number >= 2:
            
            isDivisible = False

            for index in range(2, number):
                if number % index == 0:
                    isDivisible = True
                    break
            
            if not isDivisible:
                print(number)
   

numeroPrimo()