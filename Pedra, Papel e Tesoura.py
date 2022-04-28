#Imports
from random import randint
from time import sleep
import os

#Variaveis
escolhas = ('Pedra','Papel','Tesoura')
jogador = ''
npc = randint(0,2)

#Loop
while jogador !=9:

    #Opcoes
    print('''
    Escolha uma das opções abaixo

    [0] - Pedra
    [1] - Papel
    [2] - Tesoura
    [9] - Sair

    ''')
    
    #Escolga
    jogador = int(input('Escolha um numero: '))
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #Display
    print('~x'*15)
    print()
    print(f'O Jogador jogou {format(escolhas[jogador])}')
    print(f'O Computador jogou {format(escolhas[npc])}')
    print()
    print('~x'*15)

    #Resultado
    if jogador == 0:
        
        if npc == 0:
            print()
            print('Empate')
        elif npc == 1:
            print()
            print('Computador Ganhou')
        elif npc == 2:
            print()
            print('Voce Ganhou')

    elif jogador == 1:
        
        if npc == 0:
            print()
            print('Voce Ganhou')
        elif npc == 1:
            print()
            print('Empate')
        elif npc ==2:
            print()
            print('Computador Ganhou')

    elif jogador == 2:
        
        if npc == 0:
            print()
            print('Voce Ganhou')
        elif npc == 1:
            print()
            print('Voce Ganhou')
        elif npc == 2:
            print()
            print('Computador Ganhou')
    
    #Saida
    elif jogador == 9:
        break
    #Alternativa errada
    else:
        print('Alternariva não encontrada')
