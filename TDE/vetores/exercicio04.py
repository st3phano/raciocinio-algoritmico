'''
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores
X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
devera escrever a soma dos valores encontrados nas respectivas posições X e Y.
'''

import re

def lerNumeroReal(requisicao: str) -> float:
   REGEX_REAL = r"[-+]?\d*\.?\d+"

   while (not re.fullmatch(REGEX_REAL,
                           real := input(requisicao))):
      print(f"'{real}' não é um número real!")

   return float(real)

def lerInteiro(requisicao: str) -> int:
   REGEX_INTEIRO = r"[-+]?\d+"

   while (not re.fullmatch(REGEX_INTEIRO,
                           inteiro := input(requisicao))):
      print(f"'{inteiro}' não é um número inteiro!")

   return int(inteiro)

def lerInteiroNoIntervalo(requisicao: str, inicio: int, final: int) -> int:
   while ((inteiro := lerInteiro(requisicao)) and
          ((inteiro < inicio) or (final <= inteiro))):
      print(f"'{inteiro}' não está no intervalo entre [{inicio} e {final})")

   return inteiro

###################################################################################################

TAMANHO_REAIS = 8
reais = list()
for i in range(TAMANHO_REAIS):
   reais.append(lerNumeroReal(f"Digite o {i + 1}o número real: "))

x = lerInteiroNoIntervalo(f"Digite um inteiro entre [0 e {TAMANHO_REAIS}): ", 0, TAMANHO_REAIS)
y = lerInteiroNoIntervalo(f"Digite outro inteiro entre [0 e {TAMANHO_REAIS}): ", 0, TAMANHO_REAIS)
soma = reais[x] + reais[y]
print(f"{x}o: {reais[x]} + {y}o: {reais[y]} = {soma}")
