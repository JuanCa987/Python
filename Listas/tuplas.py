"""tuplas : es una lista de elementos que pueden ser de diferentes tipos"""

student = ("Juan", "Perez", 20 , ("Perez"))

print(student.count("Perez")) #imprime el numero de veces que aparece el nombre
print(student.index("Juan")) #imprime la posicion de la primera aparicion del nombre

for i in student:
    print(i)

if "juan" in student: #comprueba si el nombre esta en la lista
    print("Juan esta aqui!") #si es asi, imprime el mensaje