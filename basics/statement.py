# if statement: es una declaracion que se ejecutara si la condicion es verdadera.
try:
    age = float(input("ingresa tu edad: "))

    if age >= 18:
        print("Eres mayor de edad")
    elif age <= 0:
        print("Introduce un numero entero positivo")
    else:
        print("Eres menor de edad")
        
except ValueError:
     print("Errrrror")

# return statement: es una declaracion que se ejecutara y devolverara un valor

def  multiplicar(a,b):
    return a * b

x = multiplicar(2,3)
print(x)