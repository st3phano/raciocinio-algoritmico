'''
Escreva um programa que crie uma lista com os números de 1 a 10 e os imprima
na tela em ordem reversa.
'''

NUMERO_INICIAL = 1
NUMERO_FINAL = 10
numeros = [n for n in range(NUMERO_INICIAL, NUMERO_FINAL + 1)]

print([n for n in reversed(numeros)])
