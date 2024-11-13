"""Duck typing: es un patron de diseño de programación donde se asume que una clase o objeto tiene un comportamiento determinado, pero no se requiere que el comportamiento sea explícito."""

class Pato:
    def speak(self):
        print("Este pato esta haciendo cuac")

    def walk(self):
        print("Este pato esta caminando")

class Gallina:

    def walk(self):
        print("Esta gallina esta caminando")
    