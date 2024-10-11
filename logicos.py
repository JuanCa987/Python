# Operadores logicos: (and,or,not) permiten combinar condiciones y evaluar expresiones que resulten en valores booleanos (True o False)

temp = int(input("Cual es la temperatura afuera: "))

if temp >= 0 and temp <= 30:
    print("La temperatura esta bien afuera")
elif temp < 0 or temp > 30:
    print("La temperatura afuera esta mal")
    print("No salga de casa")

# not se utiliza para voltear que es true a false y viceversa