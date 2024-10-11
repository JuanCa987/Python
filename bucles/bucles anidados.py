#  bucles anidados = bucles que se ejecutan dentro de otros bucles

filas = int(input("Ingresa la cantidad de filas: "))
columnas = int(input("Ingresa la cantidad de columnas: "))
simbolo =  input("Ingresa el simbolo: ")

for i in range (filas): #bucle externo
    for j in range(columnas): #bucle interno
        print(simbolo, star = "") #end = "" para que no se imprima el simbolo en una sola linea
    print()