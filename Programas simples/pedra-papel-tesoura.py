from random import randint
from time import sleep as sl

l = ("PEDRA", "PAPEL", "TESOURA")
bot = randint(0,2)
ptPlayer = 0
ptBot = 0
i = 1

print("""
---------------------
|[1] RODADA ÚNICA    |
|[2] MELHOR DE TRÊS  |
|[3] MELHOR DE CINCO |
---------------------""")
while True:
    rod = int(input("Qual sua opção? "))
    if rod == 2:
        rod = 3
        break
    elif rod == 3:
        rod = 5
        break
    elif rod != 1:
        print("Opção inválida!")
    break

sl(1)
while i <= rod:
    print("=-"*11)
    print(f"{i}ª RODADA")
    print("""Suas Opções:
    -------------
    |[1] PEDRA   |
    |[2] PAPEL   |
    |[3] TESOURA |
    -------------""")
    player = int(input("Qual a sua jogada? "))
    if player > 3 or player <=0:
        print("jogada inválida!")
    else:
        sl(0.5)
        print("JO")
        sl(0.5)
        print("KEN")
        sl(0.5)
        print("PO!!!")
        sl(0.5)
        print("=-"*11)
        print(f"""Bot jogou {l[bot]}.
Player jogou {l[player-1]}.""")
        print("=-"*11)
        if bot == 1 and player-1 == 0 or bot == 2 and player -1 == 1 or bot == 0 and player -1 == 2:
            print("Bot VENCER!")
            ptBot += 1
        elif player - 1 == bot:
            print("EMPATE!")
        else:
            print("Player VENCE!")
            ptPlayer += 1
        i += 1
        sl(1.5)

print("=-"*11)
if ptPlayer > ptBot:
    print(f"O vencedor foi o Player com {ptPlayer} pontos!")
elif ptBot > ptPlayer:
    print(f"O vencedor foi o Bot com {ptBot} pontos!")
else:
    print(f"O jogo EMPATOU com ambos tendo {ptPlayer} pontos!")
