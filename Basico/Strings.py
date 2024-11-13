myString = "longitud del string"
my2String = " segundo String"

print(len(myString)) # Longitud del string

print(myString + " " + my2String)

saltoDeLinea = "primera linea\nSegunda linea"
print(saltoDeLinea)

tabString = "\tString con tabulación"
print(tabString)

scapeString = "\tString con \n escapado"
print(scapeString)

# Formateo

name, surname, age = "Adrián", "Belarte", 34

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje

print(a)
print(b)

# División

languageSlice = languaje[1:3]
print(languageSlice)

languageSlice = languaje[1:]
print(languageSlice)

languageSlice = languaje[-2]
print(languageSlice)

languageSlice = languaje[0:6:2]
print(languageSlice)



# Reverse

reverseLanguage = languaje[::-1]
print(reverseLanguage)

# Funciones

print(languaje.capitalize()) # Pone la primera letra en mayusculas
print(languaje.upper()) # Todos los caracteres a Mayusculas
print(languaje.count("t")) # cuenta cuatas letras de `x` 
print(languaje.isnumeric()) # comprueba si es un numero
print(languaje.lower()) # Todos los caracteres a Minusculas
print(languaje.upper().isupper()) # comprueba si esta en Mayusculas
print(languaje.startswith("py")) # comprueba si empieza con `x`




