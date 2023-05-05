'''
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
'''

import re

TAMANHO_NUMEROS_INTEIROS = 20
numerosInteiros = [0] * TAMANHO_NUMEROS_INTEIROS

regexInteiro = r"-?\d+"
for i in range(TAMANHO_NUMEROS_INTEIROS):
   numeroDigitado = input(f"Digite o {i + 1}o número inteiro: ")

   # previne entradas que não sejam número inteiros
   while (re.match(regexInteiro, numeroDigitado) == None):
      numeroDigitado = input("Entrada inválida! Digite um número inteiro: ")

   numerosInteiros[i] = int(numeroDigitado)

print(set(numerosInteiros))
