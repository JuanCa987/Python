import os 
origen = "ejemplom"
destino = "C:\\Users\\Kmilo\\Documents\\UniLibre\\Visual\\python_full\\carpeta\\ejemplom"

try:
    if os.path.exists(destino):
        print(f"El {origen} ya existe en la ruta especificada")
    else:
        os.replace(origen, destino)
        print(f"El {origen} se ha movido correctamente")

except FileNotFoundError:
    print(f"El {origen} no existe")
