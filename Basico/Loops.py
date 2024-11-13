# Loops

myCondition = 0

while myCondition < 10:
    print(myCondition)
    myCondition += 2
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while myCondition < 20:
    myCondition += 1

    if myCondition == 15:
        print("Mi condición es 15")
        print("Se detiene la ejecución")
        break # Para la ejecucion auque el while pudiera continuar

    print("Mi condición es menor que 20")

print("La ejecución continúa")

# FOR

myList = [35, 24, 13, 69, 5, 5, 17]
myTuple = (35, 1.77, "Adrian", "Belarte")
mySet = {"Adrian", "Belarte", 34}
myDict = {
    "Nombre": "Adrian",
    "Apellido": "Belarte",
    "Edad": 34,
    "Lenguages": {"Python", "Swift", "Kotlin"}
}


for element in myList:
    print(element)

for element in myTuple:
    print(element)

for element in mySet:
    print(element)

for element in myDict:
    print(element)
    if element =="edad":
        print(element)
        print("Se detiene la ejecución en edad")
        break

for element in myDict.values():
    print(element)
else:
    print("el bucle para diccionarios a terminado")

for element in myDict:
    print(element)
    if element =="edad":
        print(element)
        continue # vuelve al for
else:
    print("el bucle para diccionarios a terminado")