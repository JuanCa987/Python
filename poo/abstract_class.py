from abc import ABC, abstractmethod # se importan las clases abstract y abstractmethod que se usan para crear clases abstractas
"""Abstract classes: es una clase que no puede ser instanciada directamente, sino que debe ser extender por una o más clases concretas."""
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is going...")
    def stop(self):
        print("The car is stopping...")

class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is going...")
    def stop(self):
        print("The motorcycle is stopping...")

car = Car()
motorcicle = Motorcycle()


car.stop()
motorcicle.go()
