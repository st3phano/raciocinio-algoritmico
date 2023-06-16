'''
Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
'''

import re

def lerNumeroInteiro(requisicao: str) -> int:
   REGEX_INTEIRO = r"[-+]?\d+"

   while (not re.fullmatch(REGEX_INTEIRO,
                           inteiro := input(requisicao))):
      print(f"'{inteiro}' não é um número inteiro!")

   return int(inteiro)

###################################################################################################

TAMANHO_INTEIROS = 6
inteiros = [0] * TAMANHO_INTEIROS
for i in range(TAMANHO_INTEIROS):
   inteiros[i] = lerNumeroInteiro(f"Digite o {i + 1}o número inteiro: ")

for i in range(TAMANHO_INTEIROS):
   print(f"{i + 1}o número inteiro: {inteiros[i]}")
