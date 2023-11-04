import random


def game_logic():
    computer_lives = 2
    lives = 2
    while lives > 0 and computer_lives > 0:
        user_option = input('''Elije entre:
        1) Piedra
        2) Papel
        3) Tijeras

        (Introduce el número de tu elección)

        ''')
        computer_option = random.choice(["Piedra", "Papel", "Tijeras"])
        if user_option == "1":
            user_option = "Piedra"
            if computer_option == "Tijeras":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("Felicidades, usted ha ganado!")
                computer_lives = -1
            elif computer_option == "Papel":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("La computadora ha ganado!")
                lives = -1
            else:
                print("Es un empate!")
        elif user_option == "2":
            user_option = "Papel"
            if computer_option == "Piedra":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("Felicidades, usted ha ganado!")
                computer_lives = -1
            elif computer_option == "Tijeras":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("La computadora ha ganado!")
                lives = -1
            else:
                print("Es un empate!")
        elif user_option == "3":
            user_option = "Tijeras"
            if computer_option == "Papel":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("Felicidades, usted ha ganado!")
                computer_lives = -1
            elif computer_option == "Piedra":
                print("El usuario eligió", user_option)
                print("La computadora eligió", computer_option)
                print("La computadora ha ganado!")
                lives = -1
            else:
                print("Es un empate!")
        else:
            print("Esa no es una jugada válida!")
            print('''
        Reiniciando el programa...
        
        
        ''')
            game_logic()

    if lives == 0:
        print('''
              
              Ud. ha perdido la partida.
              
              ''')
    else:
        print('''
              
              Ud. ha ganado la partida!
              
              ''')


if __name__ == "__main__":
    game_logic()
