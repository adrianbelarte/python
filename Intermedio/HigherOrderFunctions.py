### HIGHER ORDER FUNCTIONS ###

from functools import reduce


def sumOne(value):
    return value + 1

def sumFive(value):
    return value + 5

def sumTwoValuesAndAddOne(firstValue, secondValue, fSum):
    return fSum(firstValue, secondValue)

#print(sumTwoValuesAndAddOne(5, 2, sumOne))
#print(sumTwoValuesAndAddOne(5, 2, sumFive))

### CLOSURES ###

def sumTen(originalValue):
    def add(value):
        return value + 10 + originalValue
    return add

addClosure = sumTen(1)
print(addClosure(5))

numbers = [2, 5, 10, 21, 3, 30]

# MAP

def multiplyTwo(number):
    return number + 2


print(list(map(multiplyTwo, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter 

def filterGreaterTen(number):
    if number > 10:
        return True
    return False

print(list(filter(filterGreaterTen, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# REDUCE

def sumtwoValues(firstValue, secondValue):
    print(firstValue)
    print(secondValue)
    return firstValue + secondValue

print(reduce(sumtwoValues, numbers))