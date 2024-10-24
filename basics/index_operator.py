# operdaor index: devuelve el valor de un elemento en una lista (str,list,tuples,diccionarios)

name = "juan CaMILO"

"""if(name[0].islower()): # devuelve True si la primera letra es minuscula
    name = name.capitalize() # devuelve el valor de la primera letra en mayuscula

print(name)"""

first_name = name[:4].upper() # devuelve las 4 primeras letras en mayuscula
last_name = name[7:].lower() # devuelve las letras restantes en minuscula
last_character = name[-1] # solo devuelve la ultima letra

print(first_name)
print(last_name)
print(last_character)