'''
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
'''

import re

TAMANHO_NUMEROS_INTEIROS = 20
numerosInteiros = [0] * TAMANHO_NUMEROS_INTEIROS

for i in range(TAMANHO_NUMEROS_INTEIROS):
   numeroDigitado = input(f"Digite o {i + 1}o número inteiro: ")

   # demanda que o número digitado seja inteiro
   regexInteiro = r"[-+]?\d+"
   while (re.fullmatch(regexInteiro, numeroDigitado) == None):
      numeroDigitado = input("Entrada inválida! Digite um número inteiro: ")

   numerosInteiros[i] = int(numeroDigitado)

print(set(numerosInteiros))
