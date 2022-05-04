from random import randint
from time import sleep
computador = randint(0, 5)  #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei: '))  #  JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(3)                          #  ESPERA 3 SEGUNDOS
if jogador == computador:
    print('Você acertou!')
else:
    print('Eu ganhei! Eu pensei no número {} e você no número {}.'.format(computador, jogador))
    