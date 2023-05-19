'''
Escreva um programa que crie uma lista com os números de 1 a 10 elevados ao
quadrado. Em seguida, calcule a soma dos elementos da lista e imprima o
resultado.
'''

NUMERO_MIN = 1
NUMERO_MAX = 10
numeros = [n * n for n in range(NUMERO_MIN, NUMERO_MAX + 1)]
print(numeros)

somaNumeros = sum(numeros)
print(somaNumeros)
