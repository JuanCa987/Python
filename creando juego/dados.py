import random

def lanzar_dado():
    return random.randint(1, 6)

def start_game():
    print("Hola, bienvenido al juego de dados")

    while True:
        input("Presiona Enter para empezar el juego")
        resultado = lanzar_dado()
        print(f"has lanzado {resultado}")

        if resultado == 1:
            print("Ganaste")
            break
        elif resultado == 6:
            print("Perdiste")
            break
        else:
            print("Continua jugando")
            continue
start_game()