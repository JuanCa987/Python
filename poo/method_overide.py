"""Anulacion de metodos: es un mecanismo de anulacion de metodos en Python que permite reescribir el comportamiento de un metodo existente en una clase hija"""

class Animal:
    def comer(self):
        print("El animal come") #metodo de la clase padre

class Conejo(Animal):
    def comer(self): # anulacion de metodo de la clase padre
        print("Este conejo esta comiendo una zanahoria")


conejo = Conejo()

conejo.comer()

# resumiendo el codigo anterior, el metodo comer de la clase padre se anula en la clase hija con el metodo comer de la clase hija