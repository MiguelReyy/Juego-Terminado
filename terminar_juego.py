import random

def jugar_juego(): 
    """esta funcion es la principal que contiene el juego"""

    def regujabilidad():
        """esta funcion se encarga de volver a jugar cuando acaba el juego"""

        replay = input("Escribe S para volver a jugar, y N para salir del juego: ").upper()

        if replay == "S":

                jugar_juego()
        elif replay == "N":
                print("Muchas gracias por jugar. Espero verte pronto.")
                exit
        else:
                print("Introduce un caracter válido porfavor")
                regujabilidad()

    """La variable dificulty se utiliza para seleccionar una dificultad y minimum y maximum para directamente conocer el intervalo entre los numeros que tenemos que adivinar"""
    dificulty = int(input("Selecciona una dificultad. 1 para fácil, 2 para medio, 3 para díficil y 4 para imposible: "))

    if dificulty == 1:
        minimum, maximum = 0, 100
        secret_num = random.randint(minimum, maximum) 
    elif dificulty == 2:
        minimum, maximum = 0, 1000
        secret_num = random.randint(minimum, maximum) 
    elif dificulty == 3:
        minimum, maximum = 0, 1000000
        secret_num = random.randint(minimum, maximum)
    elif dificulty == 4:
        minimum, maximum = 0, 1000000000000
        secret_num = random.randint(minimum, maximum) 

    numeroadivinar = int(input(f"Tienes que adivinar un número entre {minimum} y {maximum}: "))
    """intentos es la variable par acontabilzar los intentos sumando una unidad por cada intento"""
    intentos = 0

    while True:
        intentos += 1
        if numeroadivinar == secret_num:
            print(f"Has adivinado el número: {secret_num} y te ha costado {intentos} intentos.")
            break
        elif numeroadivinar < secret_num:
            numeroadivinar = int(input("El número es muy bajo, vuelve a intentarlo: "))
        else:
            numeroadivinar = int(input("El número es muy alto, vuelve a intentarlo: "))

    regujabilidad()


if __name__ == "__main__":
    jugar_juego()