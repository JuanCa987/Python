# lista = es un tipo de dato que almacena una secuencia de elementos

comida = ["manzana", "papa", "tomate", "pera"]

# print(comida[1]) #imprime el segundo elemento de la lista

comida.append("aguacate") #agrega un elemento al final de la lista
comida.remove("papa") #elimina el segundo elemento de la lista
comida.insert(0, "cebolla") #inserta un elemento al principio de la lista
comida.pop() #elimina el ultimo elemento de la lista
comida.sort() #ordena la lista
comida.reverse() #invierte la lista
comida.clear() #elimina todos los elementos de la lista

for i in comida:
    print(i) #imprime cada elemento de la lista