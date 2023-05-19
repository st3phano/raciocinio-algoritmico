'''
Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida,
imprima apenas os números pares da lista.
'''

NUMERO_MIN = 1
NUMERO_MAX = 100
listaNumeros = [n for n in range(NUMERO_MIN, NUMERO_MAX + 1)]

numerosPares = list(filter(lambda x: x % 2 == 0, listaNumeros))
print(numerosPares)
