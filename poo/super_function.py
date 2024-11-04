"""super function: es una función que se puede llamar desde cualquier función, y que ejecuta el código de la función padre que la invoca."""

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Square(Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)
    
    def Area(self):
        return self.height * self.width

class Cube(Rectangle):
    def __init__(self, height, width, length):
        self.length = length
        super().__init__(height, width)
    
    def Volume(self):
        return self.length * self.width * self.height

square = Square(5, 5)
squareTwo = Square(2, 6)
print(square.Area())


#cube = Cube(3 , 3, 3)
# print(cube.Volume())