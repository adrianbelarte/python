# Dictionaries

myDict = dict()
my2Dict = {}

print(type(myDict))
print(type(my2Dict))

# Relacion Clave : Valor
my2Dict = {"Nombre":"Adrian", "Apellido": "Belarte", "Edad":34, 1:"Python"}
print(my2Dict)

myDict = {
    "Nombre": "Adrian",
    "Apellido": "Belarte",
    "Edad": 34,
    "Lenguages": {"Python", "Swift", "Kotlin"}
}

print(len(my2Dict))
print(len(myDict))

print(myDict["Nombre"])

myDict["Nombre"] = "David" # Actualizar dato
myDict["Calle"] = "Calle la unio" # Anydir nuevo campo

del myDict["Calle"] # Elimina un solo elemento
print("Nombre" in myDict) # Busca por clave

print(myDict.items()) # retorna el diccionario
print(myDict.keys()) # retorna las claves
print(myDict.values()) # retorna los valores

my3Dict = dict.fromkeys(("Nombre", 1, "Piso")) #Crea un diccionario sin valores
print(my3Dict)