'''
Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.
'''

import re

def lerNumeroReal(requisicao: str) -> float:
   REGEX_REAL = r"\s*[-+]?\d*\.?\d+\s*"

   while (not re.fullmatch(REGEX_REAL,
                           real := input(requisicao))):
      print(f"'{real}' não é um número real!")

   return float(real)

def preencherMatrizNumerosReais(linhas: int, colunas: int) -> list[list[float]]:
   return [[lerNumeroReal(f"Digite um número real para posição {linha + 1}x{coluna + 1}: ")
            for coluna in range(colunas)]
           for linha in range(linhas)]

def imprimirMatriz(matriz: list[list]) -> None:
   for linha in matriz:
      for coluna in linha:
         print(coluna, end='\t')
      print()

###################################################################################################

TAMANHO_REAIS = 4
reais = preencherMatrizNumerosReais(TAMANHO_REAIS, TAMANHO_REAIS)

imprimirMatriz(reais)

linhaMaiorReal = 0
colunaMaiorReal = 0
maiorReal = reais[linhaMaiorReal][colunaMaiorReal]
for l in range(TAMANHO_REAIS):
   for c in range(TAMANHO_REAIS):
      if (reais[l][c] > maiorReal):
         linhaMaiorReal = l
         colunaMaiorReal = c
         maiorReal = reais[l][c]
print(f"O maior número na matriz é {maiorReal} e está na posição {linhaMaiorReal + 1}x{colunaMaiorReal + 1}.")
