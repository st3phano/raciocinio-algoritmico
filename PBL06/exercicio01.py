'''
Escreva um programa que crie uma lista com números aleatórios e a imprima na
tela.
'''

from random import randint

NUMERO_MIN = 1
NUMERO_MAX = 100
TAMANHO_NUMEROS_ALEATORIOS = 10
numerosAleatorios = [randint(NUMERO_MIN, NUMERO_MAX) for _ in range(TAMANHO_NUMEROS_ALEATORIOS)]
print(numerosAleatorios)
