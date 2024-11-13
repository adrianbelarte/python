# Sets

mySet = set()
my2Set = {}

print(type(mySet))

my2Set = {"Adrian", "Belarte", 34}
print(len(my2Set))

my2Set.add("Stifle")
print(my2Set) # Un set no es una estructura ordenada

my2Set.add("Stifle")
print(my2Set) # No se puede repetir el mismo dato

print("Stifle" in my2Set) # realizar busqueda
my2Set.remove("Stifle") # Borrar un dato
my2Set.clear() # borra todo los elemento

del my2Set # Elimina el objeto

# No recomendado convertir un set en una list
mySet = {"Adrian", "Belarte", 34}
mylist = list(mySet)

my2Set = {"Kotlin", "Swift", "Python"}

my3Set = mySet.union(my2Set).union({"JavaScript", "C#"}) # Unir Sets
print(my3Set)

print(mySet)
print(my3Set)
print(my3Set.difference(mySet)) # busca la diferencia entre 2 sets

