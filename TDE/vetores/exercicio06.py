'''
Faça um programa que receba do usuario um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.
'''

import re

def lerNumeroReal(requisicao: str) -> float:
   REGEX_REAL = r"\s*[-+]?\d*\.?\d+\s*"

   while (not re.fullmatch(REGEX_REAL,
                           real := input(requisicao))):
      print(f"'{real}' não é um número real!")

   return float(real)

###################################################################################################

TAMANHO_REAIS = 10
reais = [lerNumeroReal(f"Digite o {i + 1}o número real: ")
         for i in range(TAMANHO_REAIS)]

menorReal = min(reais)
maiorReal = max(reais)
print(f"O menor número digitado foi {menorReal} e o maior foi {maiorReal}.")
