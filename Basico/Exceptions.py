# EXCEPTIONS

num1 = 5
num2 = 1
num = "2"

# try except
try:
    print(num1 + num)
except:
    print("Error")

# try except else
try:
    print(num1 + num)
except:
    print("Error")
else:
    # se ejecuta si no se produce una excep
    print("la ejecución continúa")
finally:
    # se ejecuta siempre
    print("la ejecución continúa..")

try:
    print(num1 + num)
except ValueError as error:
    print(error)
    print("Error de tipo ValueError")
except Exception as error:
    print(error)
    print("Error de tipo TypeError")
