import os
import shutil #shutil: es un moculo que se encarga de mover archivos
"""Eliminar archivos"""
path = "...\\carpeta\\ejemplom" #Se crea una variable path que contiene el path completo del archivo

try:
    #os.remove(path) #Elimina el archivo
    #shutil.rmtree(path) #Elimina la carpeta con los archivos dentro
    os.rmdir(path) #Elimina la carpeta
    print(f"El {path} ha sido eliminado")

except FileNotFoundError:
    print("El archivo no existe")

except PermissionError:
    print("No tiene permiso para eliminar el archivo")