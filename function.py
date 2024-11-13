"""function: es una declaracion que se ejecutara cuando se llame a la funcion """

def hello(first_name,last_name,age):
    print("hi "+first_name+" "+last_name)
    print("you are "+str(age)+"  years old")
    print("Have a good day")

hello("Juan","Ause",20)

# keywords arguments: es una forma de pasar argumentos a una funcion, que no tienen orden fijo y pueden ser pasados por cualquier orden

def hello_kw(first_name,last_name,age):
    print("hi "+first_name+" "+last_name)
    print("you are "+str(age)+"  years old")
    print("Have a good day")

hello_kw(last_name="Ause",first_name="Juan",age=20)

# scope: es la region de codigo donde se define una variable
# global: es una variable que puede ser usada en cualquier parte del codigo
# local: es una variable que solo puede ser usada en una funcion

name = "Juan"

def display_name():
    name = "juan" # Local variable
    print(name)

display_name()
print(name)