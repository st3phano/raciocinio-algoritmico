'''
Crie um programa que lê 6 valores inteiros, armazene-os em um vetor e,
em seguida, mostre na tela os valores lidos na ordem inversa.
'''

import re

TAMANHO_VALORES_INTEIROS = 6
valoresInteiros = [0] * TAMANHO_VALORES_INTEIROS
for i in range(TAMANHO_VALORES_INTEIROS):
   valorDigitado = input(f"Digite o {i + 1}o valor inteiro: ")

   # exige que o valor digitado seja inteiro
   inteiroRegex = r"-?\d+"
   while (re.fullmatch(inteiroRegex, valorDigitado) == None):
      valorDigitado = input(f"Valor inválido!\nDigite o {i + 1} valor inteiro: ")
   valoresInteiros[i] = int(valorDigitado)

for i in range(TAMANHO_VALORES_INTEIROS - 1, -1, -1):
   print(valoresInteiros[i], end=' ')
print()
