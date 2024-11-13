### REGULAR EXPRESSIONS ###

import re 

myString = "Esta es la lección número 7: Expresiones Regulares"
myOtherString = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", myString, re.I)


if not(match == None):
    print(match)    
    start, end = match.span()
    print(myString[start:end])  


print(re.match("Esta es la lección", myOtherString))
print(re.match("Expresiones Regulares", myString))

# Search

search = re.search("lección", myString, re.I)
print(search)
start, end = match.span()
print(myString[start:end])  

# Findall

findall = re.findall("lección", myString)
print(findall)

# Split

print(re.split(":", myString))

# Sub

print(re.sub("[l|L]ección", "LECCIÓN", myString))
print(re.sub("Expresiones Regulares", "RegEx", myString))

# Patterns

pattern = r'[lL]ección'
print(re.findall(pattern, myString))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, myString))

pattern = r'[0-9]'
print(re.findall(pattern, myString))

# Email validation regular expression
email = "adrian.belarte.it@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.findall(pattern, email))
print(re.search(pattern, email))