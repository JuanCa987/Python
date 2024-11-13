"""def  hello(): #definicion de funcion
    print("Holaaa") 

h = hello #asignacion de funcion

h()"""

# say = print

# say("I am happy")

"""Funciones de orden superior: son funciones que no tienen una definición explícita, sino que se definen mediante la llamada a otra función."""

def speak_up(text):
    return text.upper()

def speak_softly(text):
    return text.lower()

def hello(func): 
    text = func("Holaaa") 
    print(text) 

hello(speak_up)
hello(speak_softly)

#devuelve el valor de la funcion

def divider(x): 
    def divide(y): 
        return y / x 
    return divide 

divisor = divider(2)
print(divisor(10))

