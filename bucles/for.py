import time #import time es una libreria que nos permite usar funciones de tiempo

#  for loop = es un bluce que ejecutara un bloque de codigo una cantidad limitada de veces
#  while = unlimited
#  for = limited

# for i in range(10):
#     print(i + 1) 

# for i in range(50, 100 + 1,2): entre el rango de 50 y 100 y el paso 2 (incremento)
    # print(i)

# for i in "Juan camilo": el bucle intera una cadena de caracteres y ejecutara el bloque de codigo una vez por cada caracter
    # print(i)

for  seconds in range(10, 0, -1): #for iterara el bloque de codigo entre el rango de 10 y 0 y el paso -1 (decremento)
    print(seconds)
    time.sleep(1)  #sleep es una funcion que se ejecutara cada segundo
print("Feliz Navidad") 