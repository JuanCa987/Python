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