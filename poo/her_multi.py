"""Herencia multinivel: herencia de clases de una a dos niveles """

class Organismo: # clase padre
    vivo = True

class Animal(Organismo): # clase que hereda de Organismo 
    def comer(self):
        print("Este animal come......")

class Gato(Animal): # clase que hereda de Animal
    def maullar(self):
        print("Este gato maulla.....")

gato = Gato()
gato.comer()
gato.maullar()

# La herencia de clases de una a dos niveles es posible, pero no es recomendable.

"""Herencia multiple: es un concepto en el que una clase puede heredar atributos y métodos de más de una clase base. 
Esto significa que una sola clase puede derivarse de múltiples clases parentales, combinando las funcionalidades y comportamientos de todas ellas."""

class Presa:
    def huir(self):
        print("Esta presa huye...")

class Depredador:
    def cazar(self):
        print("Este depredador caza...")

class Conejo(Presa):
    pass

class Halcon(Depredador):
    pass

class Pez(Presa, Depredador):
    pass

conejo = Conejo() #Objeto de la clase conejo
halcon = Halcon()
pez = Pez()

conejo.huir()
halcon.cazar()
pez.cazar()