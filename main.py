import random


def roll_one_dice(dice_to_roll):
    if dice_to_roll <= 3:
        dice_to_roll = random.randint(1, 6)
    else:
        return dice_to_roll
    return dice_to_roll


feedback = None


def play(num_simulations):
    global feedback
    juan_wins = 0
    maria_wins = 0
    tie = 0

    for _ in range(num_simulations):
        total_points_juan = 0
        total_points_maria = 0
        
        dice1_juan = random.randint(1, 6)
        dice2_juan = random.randint(1, 6)
        
        if dice1_juan or dice2_juan == 4:
            if dice1_juan == 4:
                roll_one_dice(dice2_juan)
            else:
                roll_one_dice(dice1_juan)
        else:
            dice1_juan = random.randint(1, 6)
            dice2_juan = random.randint(1, 6)
        if dice1_juan or dice2_juan == 4:
            if dice1_juan == 4:
                total_points_juan = dice2_juan
            else:
                total_points_juan = dice1_juan
        dice1_maria = random.randint(1, 6)
        dice2_maria = random.randint(1, 6)
        if dice1_maria or dice2_maria == 4:
            if dice1_maria == 4:
                if dice2_maria > total_points_juan:
                    total_points_maria = dice2_maria
                else:
                    if dice2_maria < total_points_juan:
                        dice2_maria = random.randint(1, 6)
                        total_points_maria = dice2_maria
                    else:
                        if dice2_maria == total_points_juan and dice2_maria >= 4:
                            total_points_maria = dice2_maria

            else:
                if dice1_maria > total_points_juan:
                    total_points_maria = dice1_maria
                    if dice1_maria < total_points_juan:
                        dice1_maria = random.randint(1, 6)
                        total_points_maria = dice1_maria
                    else:
                        if dice1_maria == total_points_juan and dice1_maria >= 4:
                            total_points_maria = dice1_maria
            if total_points_juan > total_points_maria:
                juan_wins += 1
                if feedback:
                    print("Juan gana el juego")
            elif total_points_juan < total_points_maria:
                maria_wins += 1
                if feedback:
                    print("María gana el juego")
            else:
                tie += 1
                if feedback:
                    print("El juego resulta en empate")

    return {"Juan": juan_wins, "Maria": maria_wins, "Empate": tie}


def init():
    global feedback

    print("Tarea 2 de Probabilidad y Estadística aplicada")
    print("----------------------------------------------")
    print("¿Desea activar los comentarios de cada juego?")
    while True:
        feedback = input("S/N: ")
        if feedback.lower() == "s":
            print("Comentarios activados")
            feedback = True
            break
        elif feedback.lower() == "n":
            print("Comentarios desactivados")
            feedback = False
            break
        else:
            print("Opción no válida")

    while True:
        print("¿Desea ejecutar 1000 simulaciones?")
        option = input("S/N: ")
        if option.lower() == "s":
            results = play(1000)
            print("Resultado de 1000 simulaciones")
            print("Juan: ", results["Juan"]/1000)
            print("Maria: ", results["Maria"]/1000)
            print("Empate: ", results["Empate"]/1000)
            break
        elif option.lower() == "n":
            break
        else:
            print("Opción no válida")

    while True:
        print("¿Desea ejecutar 10000 simulaciones?")
        option = input("S/N: ")
        if option.lower() == "s":
            results = play(10000)
            print("Resultado de 10000 simulaciones")
            print("Juan: ", results["Juan"]/10000)
            print("Maria: ", results["Maria"]/10000)
            print("Empate: ", results["Empate"]/10000)
            break
        elif option.lower() == "n":
            break
        else:
            print("Opción no válida")

    while True:
        print("¿Desea ejecutar 100000 simulaciones?")
        option = input("S/N: ")
        if option.lower() == "s":
            results = play(100000)
            print("Resultado de 100000 simulaciones")
            print("Juan: ", results["Juan"]/100000)
            print("Maria: ", results["Maria"]/100000)
            print("Empate: ", results["Empate"]/100000)
            break
        elif option.lower() == "n":
            break
        else:
            print("Opción no válida")

    print("Fin de las simulaciones")


init()
