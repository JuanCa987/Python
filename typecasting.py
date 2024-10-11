"""TypeCasting: Es el proceso de convertir una variable de un tipo de dato a otro
str(), int(), float(), bool(). others: list(), tuple(), set(), dict(), """

name = "Corintio code"
number = "10"
age = 20
gpa = 3.5
is_student = 1

#int()
number_int = int(number) #convierte la cadena a entero
print(number_int) #salida: 10 en entero

#float()
gpa_float = float(number) #De cadena a flotante
print(gpa_float)

#str()
age_str = str(age) #De entero a cadena
print(age_str)

#bool()
is_student_bool = bool(is_student)
print(is_student_bool)

#list()
n = (1,2,3)
list = list(n) #Convierte una cadena o tupla a una lista
print(list)

#tuple()
list = [1,2,3]
tupla = tuple(list) #Convierte la lista a tupla
print(tupla)

#set() Convierte una secuencia o iterable en un conjunto, eliminando duplicados
lista = [1,2,3,1]
conjunto = set(lista)
print(conjunto)

#dict() Convierte una secuencia de pares clave-valor en un diccionario
lista_pares = [("a",1),("b",2)]
diccionario = dict(lista_pares)
print(diccionario)

