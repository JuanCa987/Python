# dictionary =  es un tipo de dato que almacena pares clave-valor
# Los pares clave-valor se llaman diccionarios
# Los diccionarios se pueden crear de dos maneras:
# 1. Con la funcion dict()
# 2. Con el operador de asignacion

capitals = {"France": "Paris", # clave: France, valor: Paris
            "Spain": "Madrid", 
            "Germany": "Berlin"}

capitals.update({"USA": "Washington DC"}) # actualiza el diccionario
capitals.update({"UK": "London"}) # agrega un nuevo elemento
capitals.pop("France") # elimina el elemento con la clave "France"

print(capitals.get("France")) # devuelve el valor asociado a la clave "France"
print(capitals.keys()) # devuelve una lista de claves
print(capitals.values()) # devuelve una lista de valores
print(capitals.items()) # devuelve una lista de pares clave-valor

# capitals.clear()
# print(capitals["France"]) 

for key,value in capitals.items():
    print(key, value)