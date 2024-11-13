myString: str = "esto es un string"
print(myString)

myInt: int = 5
print(myInt)
str(myInt) # convierte a String
type(myInt) # ver tipo de dato

myBool = False
print(myBool)

# Concatenacion de variables
name, apellidos, edad = "Adrian","Belarte Zapata", 34
print("hola me llamo:", name, apellidos, "y tengo", edad, "anyos")

# Funciones del sistema
print(len(myString)) # Cuenta caracteres

# Inputs
name = input("Cuál es tu nombre?")
age = input("Que edad tienes?")
print(name)
print(age)

# Tipos de datos
print(type("Dato str")) # Tipo str
print(type(5))          # Tipo int
print(type(1.5))        # Tipo float
print(type(3 + 1j))     # Tipo complex
print(type(True))       # Tipo bool


