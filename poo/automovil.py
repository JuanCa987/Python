class Auto:
    
    ruedas = 4 # variable de clase se declaran fuera del constructor, se pueden acceder a ellas desde cualquier metodo

    def __init__(self,marca,modelo,color,ano): #constructor
        self.marca = marca #atributo
        self.modelo = modelo # las variables de instancia se declaran dentro del constructor, solo pueden accederse desde el constructor
        self.color = color
        self.ano = ano

    def conducir(self): #metodo
        print("El automovil se encuentra conduciendo")
    
    def apagar(self):
        print("El automovil se encuentra apagando")