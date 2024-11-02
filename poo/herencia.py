#Herencia: es un mecanismo de herencia de clases en Python que permite crear nuevas clases que heredan de una o más clases existentes
class Animal(): #clase padre
    def __init__(self,nombre,edad,peso): #constructor
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    life = True

    def eat(self):
        print("El animal come")
    
    def sleep(self): #metodo heredado
        print("El animal duerme")
    
class Conejo(Animal): #clase hija
    def run(self): #metodo unico de la clase hija (no heredado)
        print("El conejo corre")

class Pez(Animal): #clase hija
    def swim(self): #metodo unico
        print("el pez nada")

class Halcon(Animal): #clase hija
    def fly(self):
        print("El Halcon vuela")

conejo = Conejo("Emilio",5,100) #instancia de la clase hija
pez = Pez("maria",2,10)
halcon = Halcon("juan",3,200)

print(conejo.nombre) #llama al metodo de la clase padre
pez.swim() #llama al metodo de la clase hija