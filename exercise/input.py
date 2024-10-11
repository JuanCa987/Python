#Exercise 1: calcular el area de un rectnagulo

length = float(input("Ingresa la longitud: "))
width = float(input("ingresa el ancho:"))

area = length * width

print(f"el area del rectangulo es: {area} cm")

#exercise 2: programar un carrito de compras(item,price,quantiy)
item = input("ingrese un producto: ")
price = float(input("cual es su precio: "))
quantity = float(input("cuantos le gustaria llevar: "))

total = price * quantity

print(f"va llevar {quantity} {item}/s con un total de ${total}")