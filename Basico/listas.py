# LISTS

myList = list()
my2list = []

print(len(myList))

myList = [35,24,62,52,30,17]
print(myList)
print(len(myList))

my2list = [35, 1.77, "Adrián", "Belarte"]
print(type(my2list))

print(my2list[0])
print(my2list[1])
print(my2list[-1])
print(my2list[-3])
print(my2list.count(30)) # retorna en número de occurencias

age , height, name, surname = my2list
print(name)

print(myList + my2list)

myList.append(5) # anyadir un elemento al final de la lista
myList.insert(1,69) # anyadir un elemento en una posición.

myList.remove(24) # elimina un elemento en concreto
print(myList)

print(myList.pop()) # Elimina el ultimo elemento por defecto
print(myList)

myPop = myList.pop()
print(myPop)

print(myList.pop(2)) # Elimina el x elemento por indice
print(myList)

myList[0] = 15 # cambia un valor por otro de la lista por indice
print(myList)

my3list = myList.copy() # copia una lista

my3list.reverse() # da la vuelta a la lista
print(my3list)

my3list.sort() # ordenacion de mayor a menor
print(my3list)

print(my3list[1:3]) # sublistas

myList.clear() # limpia la lista

