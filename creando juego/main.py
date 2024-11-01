import random

lista = ["piedra", "papel", "tijera"]

while True: # Se usa while True para que el juego se repita
    system = random.choice(lista) 
    player = None # player es una variable global

    while player not in lista: 
        player = input("Elige piedra, papel o tijera: ").lower() # se pide al usuario que elija una de las opcioneslower() convierte a minusculas
 
    print(f"El jugador ha elegido: {player}")
    print(f"el sistema ha elegido: {system}")

    if player == system: # Si el jugador y el sistema tienen la misma opcion, se imprime "empate"
        print("Empate")
    elif player == "piedra": # Si el jugador elige piedra
        if system == "papel": 
            print("El systema gana") 
        if system == "tijera":
            print("el jugador gana") 
    elif player == "papel": # Si el jugador elige papel
        if system == "piedra":
            print("el jugador gana") 
        if system == "tijera":
            print("El systema gana")
    elif player == "tijera": # Si el jugador elige tijera
        if system == "piedra":
            print("El systema gana")
        if system == "papel":
            print("el jugador gana")

    play_again = input("Quieres jugar otra vez? (s/n): ") # Se pide al usuario si quiere jugar otra vez
    if play_again != "s": # Si el usuario no quiere jugar otra vez, se sale del juego
        break #break termina el bucle
print("Gracias por jugar!")