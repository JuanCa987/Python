"""str.format: es una funcion que permite formatear una cadena de texto con variables"""

number = 10000

print("the number is {:.3f}".format(number)) #usando el formato de cadena :.3f es un formato de float que permite que el numero se muestre con 3 decimales
print("the number is {:,}".format(number)) # la coma es el separador decimal
print("the number binary is {:b}".format(number)) # b es el formato de binario
print("the number octal is {:o}".format(number)) # o es el formato de octal
print("the number hexadecimal is {:X}".format(number)) # X es el formato de hexadecimal
print("the number integer is {:d}".format(number)) # d es el formato de entero
print("the number scientific notation is {:e}".format(number)) # e es el formato de notacion cientifica 