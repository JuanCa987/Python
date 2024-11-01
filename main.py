#Asi se hace una comentario en python
"""Asi tambien se puede hacer un comentario en python
para varias lineas"""

try: 
    numerator =int(input("Introduce un numero: "))
    denominator = int(input("Introduce otro numero: "))
    
    result= numerator/denominator
    print(f"el resultado es {result}")
#except es una sentencia de control de excepciones
except ZeroDivisionError: #Se puede usar el mismo nombre que el error
    print("No se puede dividir por cero, idiota!")

except ValueError:
    print("Ha ocurrido un error")