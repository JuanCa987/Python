"""set: es una coleccion de elementos que no pueden repetirse """

utensilios = {"cuchara", "tenedor", "cuchillo"}
platos = {"plato", "pardo", "plano" ,"cuchara"}

utensilios.add("lapicero") # agrega un elemento a la lista
utensilios.remove("cuchara") # remueve el elemento de la lista # utensilios.clear()
platos.update("utensilios") # actualiza la lista

mesa = utensilios.union(platos) # crea un nuevo set con los elementos de ambas listas

print(utensilios.intersection(platos)) # crea un nuevo set con los elementos que estan en ambas listas
print(utensilios.difference(platos)) # crea un nuevo set con los elementos que estan en la primera lista pero no en la segunda
