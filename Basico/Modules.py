# MODULES


import  Functions #importa el modulo entero
from Classes import Persona #importa solo una parte del modulo
import math # importa modulos del sistema
from math import pi as piValue # importa una parte del modulo y le asigna un nombre concreto

Functions.sum2values(5,3)

p1 = Persona("Zulema", "Guimenez")
print(f"{p1.name} {p1.surname}")

print(piValue)
print(math.pow(2,8))


