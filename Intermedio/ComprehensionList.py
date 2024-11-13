### LIST COMPREHENSION ###

myOriginalList = [35, 24, 62, 52, 30, 17]

myList = [i for i in myOriginalList]
print(myList)

myList2 = [i for i in range(8)] # Crear un rango de lista
print(myList2)

myNameList = ["Adrian", "Pedro", "Haydee", "David", "Rosario"]

def sumFive(number):
    return number + 5

mySumList = [sumFive(i) for i in range(8)]
print(mySumList)   


