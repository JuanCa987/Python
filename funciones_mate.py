import math

#Estas funciones vienen predefinidas en Python y no requieren importar ningún módulo.
x = 10.65123
y = 9
z =2

result = abs(x) # Retorna el valor absoluto de un número.
result = max(x,y,z) # Retorna el valor máximo entre un conjunto de valores.
result = min(x,y,z) # Retorna el valor minimo entre un conjunto de valores.
result = pow(x,y) # Eleva x a la potencia de y. Es equivalente a x ** y.
result = round(x, 2) # Redondea x al número de decimales especificado por n.

"""Para usar estas funciones, primero debes importar el módulo math."""

# math.sqrt(x) – Raíz cuadrada
result = math.sqrt(y)

# math.ceil(x) – Redondear hacia arriba
result = math.ceil(x)

# math.floor(x) – Redondear hacia abajo
result = math.floor(x)

# math.pi – Valor de Pi
result = math.pi

# math.e – Constante de Euler
result = math.e

# math.log(x[, base]) – Logaritmo
result = math.log(x, 2)  #logaritmo en base 2 


# print(result)

# example

radio = float(input("ingresa el radio del circulo: "))

area = math.pi * pow(radio, 2)

print(f"el area del circulo es de {area} cm")