# *args: son parametros que pueden recibir mas de un valor en una funcion y son pasados por orden de aparicion

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

# **kwargs:La función recibe kwargs como un diccionario, donde cada clave es el nombre del argumento, y cada valor es el valor correspondiente.
def hello(**names): 
    print("Hello", end=" ") 
    for key,value in names.items(): # itera sobre el diccionario
        print(value, end=" ") # imprime el valor

hello(title="Mr.", first="juan", middle="camilo", last="Ausecha") 