# Conditionals

myCondition = True

if myCondition:
    print("Se ejecuta la condición del if")

myCondition = 10

if myCondition == 11:
    print("Se ejecuta la condición del segundo if")


if myCondition > 10 and myCondition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor que 10 o mayor que 20")

myString = ""

if not myString:
    print("Mi cadena de texto es vacía")

if myString == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")
    
print("La ejecución continúa")