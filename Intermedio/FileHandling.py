### File Handling ###

import os

# .txt file

txtFile = open("Intermedio/MyFile.txt", "w+") #Leer y Escribir

#print(txtFile.read()) # Lee todo el fichero
#print(txtFile.read(10)) # lee los 10 primeros caracteres 
#print(txtFile.readline()) # Lee el fichero linea a linea
#print(txtFile.readlines()) # Lee el fichero y cada linea la pone en un array
#txtFile.write ("\nKotlin")
#print(txtFile.readline())

txtFile.close()

#os.remove("Intermedio/MyFile.txt")

# .json  file

import json

jsonFile = open("Intermedio/MyFile.json", "w+")

jsonTest = {
    "name":"Adrian",
    "surname":"Belarte",
    "age":35,
    "languages":["Python", "Swift", "Java"]
}

json.dump(jsonTest, jsonFile, indent = 2)

for line in jsonFile.readlines():
    print(line)

jsonDict = json.load(open("Intermedio/MyFile.json"))
print(jsonDict)

# .csv file

import csv

csvFile = open("Intermedio/MyFile.csv", "w+")
csvWrite = csv.writer(csvFile)
csvWrite.writerow(["name", "surname", "age", "language"])
csvWrite.writerow(["Adrian","Belarte", 34, "Python"])

csvFile.close()

with open("Intermedio/MyFile.csv") as myOtherFile:
    for line in myOtherFile.readlines():
        print(line)
        
# xlsx file

# xml file

import xml