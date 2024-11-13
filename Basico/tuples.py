# Tuples, son inmutables

myTuple = tuple()
my2Tuple = ()

myTuple = (35, 1.77, "Adrian", "Belarte")
my2Tuple = ("Valencia", "Spain")

print(myTuple)
print(type(myTuple))

print(myTuple.count("Adrian"))
print(myTuple.index(35))

# myTuple[1] = 1.80  no se pueden insertar datos

my3Tuple = myTuple + my2Tuple
print(my3Tuple)

print(my3Tuple[3:6]) # buscar datos en una tupla

myTuple = list(myTuple) # cambiar de tupla a list
print(myTuple)

del myTuple # elimina la definicion de la variable