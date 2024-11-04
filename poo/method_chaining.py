"""method chaining: es un concepto en el que se puede llamar a métodos de una clase, pasándole como parámetros a otros métodos de la misma clase."""

class Car:
    def run(self):
        print("The car is running...")
        return self

    def stop(self):
        print("The car has stopped...")
        return self

    def accelerate(self):
        print("The car is accelerating...")
        return self
    
    def turn_off(self):
        print("The car has turned off...")
        return self # El método turn_off() devuelve el objeto Car

car = Car()
car.run().accelerate().stop()
# El método run() se puede llamar a través de stop() y accelerate() a través del método run().

car.stop().accelerate()

car.run()\
    .accelerate()\
        .stop()\
            .turn_off()