#//////////////////////////////////
def new_game():
    answers = []
    answer_correct = 0
    num_questions = 0

    for key in question:  # itera sobre las preguntas
        print("//////////////////////////////////")
        print(key)  # imprime la pregunta
        for i in options[num_questions]:  # itera sobre las opciones
            print(i)  # imprime las opciones
        
        answer = input("Ingresa tu respuesta (A, B, C, D): ").upper()  # pide la respuesta
        answers.append(answer)  # agrega la respuesta al final de la lista

        answer_correct += check_answer(question[key], answer)  # comprueba si la respuesta es correcta
        
        num_questions += 1  # aumenta el número de preguntas
    
    display_score(num_questions, answers, answer_correct)  # pasa el puntaje correcto a la función de mostrar resultados
#//////////////////////////////////
def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:  # si la respuesta es correcta
        print("Correcto")
        return 1  # retorna 1 si es correcto
    else:
        print("Incorrecto")
        return 0  # retorna 0 si es incorrecto
#//////////////////////////////////
def display_score(num_questions, answers, answer_correct):
    print("//////////////////////////////////")
    print("RESULTADOS")
    print("//////////////////////////////////")

    print("Respuestas correctas: ", end="")
    for key in question:
        print(question[key], end=" ")  # imprime las respuestas correctas
    print()

    print("Tus respuestas: ", end="")
    for i in answers:
        print(i, end=" ")  # imprime las respuestas del jugador
    print()

    points = int((answer_correct / num_questions) * 100)  # calcula los puntos
    print("Puntos totales: ", points)
#//////////////////////////////////
def play_again():
    again = input("¿Quieres jugar otra vez? (s/n): ").lower()
    return again == "s"  # retorna True si quiere jugar de nuevo, False si no
#//////////////////////////////////

# Diccionario de preguntas y respuestas correctas
question = {
    "¿Qué idioma se habla en Brasil?: ": "A",
    "¿Cuál es el océano más grande del mundo?: ": "B",
    "¿Cuál es la estrella más brillante del universo?: ": "C",
    "¿Cuál es el segundo país más grande del mundo?: ": "D",
}

# Opciones de respuesta para cada pregunta
options = [
    ["A. Portugués", "B. Inglés", "C. Español", "D. Italiano"],
    ["A. Atlántico", "B. Pacífico", "C. Ártico", "D. Índico"],
    ["A. La luna", "B. Alfa Centauri", "C. El sol", "D. Ninguna"],
    ["A. Argentina", "B. Rusia", "C. USA", "D. China"]
]

new_game()  # Inicia el juego

while play_again():  # Verifica si el jugador quiere jugar de nuevo
    new_game()
print("¡Gracias por jugar!")
