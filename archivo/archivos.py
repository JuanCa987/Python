import os #Se importa el modulo os: el modulo os es el que se encarga de manejar los archivos

path = os.path.join(os.getcwd(), "archivo.txt") #Se crea una variable path que contiene el path completo del archivo
archivo = open(path, "w") #Se abre el archivo
archivo.write("Este es un archivo de ejemplo, de como crearlo") #Se escribe en el archivo
carpeta = os.path.join(os.getcwd(), "carpeta") #Se crea una variable carpeta que contiene el path completo de la carpeta
"""os.mkdir(carpeta) #Se crea la carpeta"""

if os.path.exists(path): #Se comprueba si el archivo existe
    print("El archivo existe")
    if os.path.exists(carpeta): #Se comprueba si la carpeta existe
        print("La carpeta existe")
else:
    print("El archivo no existe")

"""Leer archivos de texto"""
try:
    with open("archivo.txt") as archivo:
        print(archivo.read())

except FileNotFoundError:
    print("El archivo no existe")

"""Escribir archivos de texto"""
texto = "Hola\nEste texto ha cambiado\nun saludo"

with open("archvivo.txt", "w") as archivo: #w es para escribir
    archivo.write(texto) #Se escribe el texto

import shutil #Se importa el modulo shutil para copiar archivos
"""Copiando archivos"""
#copy file: copia un archivo a otro
#copy()
#copy2()
shutil.copyfile("test.txt", "copytest.txt") #Se copia el archivo test.txt a copytest.txt

