from automovil import Auto

car_one = Auto("Nissan","Maxima","azul",2022)
car_two =  Auto("Ford","Mustang","rojo",2021)


print(car_one.ruedas)

print(car_two.marca)
print(car_two.modelo)
print(car_two.color)
print(car_two.ano)

car_one.conducir()
car_two.apagar()

"""Pasar un objeto como argumento"""

class Car:
    color = None

class Motorcycle:
    color = None

def color_car(vehicle, color):
    vehicle.color = color

car_one = Car()
car_two = Car()
car_three = Car()
motorcycle = Motorcycle()

color_car(car_one, "rojo")
color_car(car_two, "azul")
color_car(car_three, "verde")
color_car(motorcycle, "negro")

print(car_one.color)
print(car_two.color)
print(car_three.color)
print(motorcycle.color)