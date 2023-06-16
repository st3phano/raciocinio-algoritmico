'''
Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado dos
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem
10 elementos cada. Imprimir todos os conjuntos.
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
reais = [0] * TAMANHO_REAIS
reaisAoQuadrado = [0] * TAMANHO_REAIS
for i in range(TAMANHO_REAIS):
   reais[i] = lerNumeroReal(f"Digite o {i + 1}o número real: ")
   reaisAoQuadrado[i] = reais[i] ** 2

for i in range(TAMANHO_REAIS):
   print(f"{reais[i]} ^ 2 = {reaisAoQuadrado[i]}")
