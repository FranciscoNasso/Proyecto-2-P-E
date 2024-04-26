import random

def main():
    puntosTotalesJuan = 0
    puntosTotalesMaria = 0
    dado1Juan = random.randint(1, 6)
    dado2Juan = random.randint(1, 6)
    if dado1Juan or dado2Juan == 4:
        if dado1Juan == 4:
            tira1dado(dado2Juan)
        else:
            tira1dado(dado1Juan)
    else:
        dado1Juan = random.randint(1, 6)
        dado2Juan = random.randint(1, 6)
    if dado1Juan or dado2Juan == 4:
        if dado1Juan == 4:
            puntosTotalesJuan = dado2Juan
        else:
            puntosTotalesJuan = dado1Juan
    dado1Maria = random.randint(1, 6)
    dado2Maria = random.randint(1, 6)
    if dado1Maria or dado2Maria == 4:
        if dado1Maria == 4:
            if dado2Maria > puntosTotalesJuan:
                puntosTotalesMaria = dado2Maria
            else:
                if dado2Maria < puntosTotalesJuan:
                    dado2Maria = random.randint(1, 6)
                    puntosTotalesMaria = dado2Maria
                else:
                    if dados2Maria == puntosTotalesJuan and dado2Maria >= 4:
                        puntosTotalesMaria = dado2Maria
                
        else:
            if dado1Maria > puntosTotalesJuan:
                puntosTotalesMaria = dado1Maria
                if dado1Maria < puntosTotalesJuan:
                    dado1Maria = random.randint(1, 6)
                    puntosTotalesMaria = dado1Maria
                else:
                    if dado1Maria == puntosTotalesJuan and dado1Maria >= 4:
                        puntosTotalesMaria = dado1Maria
        if puntosTotalesJuan > puntosTotalesMaria:
            print("Gana Juan")
        else:
            if puntosTotalesJuan < puntosTotalesMaria:
                print("Gana Maria")
            else:
                print("Empate")





def tira1dado(dadoATirar):
    if dadoATirar <= 3:
        dadoATirar = random.randint(1, 6)
    else:
        return dadoATirar
    return dadoATirar