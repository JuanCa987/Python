"""map es una funcion que toma una lista y devuelve una lista con los elementos transformados"""
store = [("Camisa", 20.00),
         ("Pantalon", 25.00),
         ("Zapatos", 10.00),
         ("medias", 50.00)]

fun_euro = lambda date: (date[0], date[1] * 0.96) #transforma el precio de una lista
#lambda es una funcion anónima

store_two = map(fun_euro, store) #map devuelve una lista con los elementos transformados

for i in store_two:
    print(i)

""""funcion fliter es una funcion que devuelve una lista con los elementos que cumplen una condición"""

friends = [("Juan", 22),
           ("Pedro", 19),
           ("Lucy", 25),
           ("Jorge", 17),
           ("Alex", 16)]

age = lambda date: date[1] >= 18 #filtra los elementos que cumplen una condición

friends_drink = filter(age, friends) #filter devuelve una lista con los elementos que cumplen la condición

for i in friends_drink:
    print(i)

"""reduce es una funcion que toma una lista y devuelve un solo valor"""
#reduce(fucnion, iterable)

letters = ["H", "o", "l", "a", "M", "u", "n", "d", "o", "!"]

import functools #importa la funcion reduce

word = functools.reduce(lambda x, y : x + y, letters) #reduce devuelve un solo valor
print(word)