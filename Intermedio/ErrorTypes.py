### Error TYPES ###

# SyntaxasError

#print "hola comunidad"
print("hola comunidad")

# NameError
language = "Spanish"
print(language)

# IndexError
myList = [35,24,62,52,30,17]
print(myList[0])
print(myList[5])
print(myList[-1])
#print(myList[6]) # fuera de rango

# ModuleNotError
#import maths # descomentar para erro
import math

# AttributeError
#print(math.PI) #Descomentar para Error
print(math.pi)

# KeyError
myDict = {"Nombre":"Adrian", "Apellido": "Belarte", "Edad":34, 1:"Python"}
print(myDict["Edad"])
#print(myDict["Apelido"]) #Descomentar para Error

# TypeError
#print(myList["0"]) # Descomentar para Error
print(myList[0])

# Import Error
#from math import PI # Descomentar para Error
from math import pi

# ValueError

myInt = int("10")
#myInt = int("10 anyos")  # Descomentar para Error
print(type(myInt))
