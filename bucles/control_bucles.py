""""Control de bucles: es un bloque de codigo que se ejecutara una vez o varias veces"""
# break: es un comando que se ejecutara cuando se desea salir de un bucle
# continue: es un comando que se ejecutara cuando se desea saltar a la siguiente iteracion del bucle
# pass: es un comando que se ejecutara cuando se desea hacer nada en un bucle

while True: 
    salir = input("Desea salir del bucle? (s/n)") 
    if salir == "s": #si no se escribe nada, el bucle se ejecutara infinitamente
        break #break es un comando que se ejecutara cuando se desea salir de un bucle

cedula = "1.234.567.890"

for i in cedula: 
    if i == ".": # remueve el punto decimal
        continue #continue es un comando que se ejecutara cuando se desea saltar a la siguiente iteracion del bucle
    print(i, end="") 

for i in range(1, 21): 
    if i == 10: # salta la iteracion 10
        continue #continue es un comando que se ejecutara cuando se desea saltar a la siguiente iteracion del bucle
    print(i)