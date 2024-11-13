### LAMBDAS ###

sumTwoValues = lambda firstValue, secondValue: firstValue + secondValue

print(sumTwoValues(2, 4))

multiplyValues = lambda firstValue, secondValue: firstValue * secondValue - 3
print(multiplyValues(2,4))

def sumValues(value):
    return lambda firstValue, secondValue: firstValue + secondValue + value

print(sumValues(5)(2,4))
