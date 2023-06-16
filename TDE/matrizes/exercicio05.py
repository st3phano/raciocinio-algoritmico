'''
Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca
desse valor na matriz e, ao final, escrever a localizacão (linha e coluna) ou uma mensa-
gem de “não encontrado”.
'''

import re

def lerNumeroInteiro(requisicao: str) -> int:
   REGEX_INTEIRO = r"\s*[-+]?\d+\s*"

   while (not re.fullmatch(REGEX_INTEIRO,
                           inteiro := input(requisicao))):
      print(f"'{inteiro}' não é um número inteiro!")

   return int(inteiro)

def preencherMatrizNumerosInteiros(linhas: int, colunas: int) -> list[list[int]]:
   return [[lerNumeroInteiro(f"Digite um número inteiro para posição {linha + 1}x{coluna + 1}: ")
            for coluna in range(colunas)]
           for linha in range(linhas)]

###################################################################################################

TAMANHO_INTEIROS = 5
inteiros = preencherMatrizNumerosInteiros(TAMANHO_INTEIROS, TAMANHO_INTEIROS)

x = lerNumeroInteiro("Digite um número inteiro qualquer: ")

xEstaNaMatriz = False
for l in range(TAMANHO_INTEIROS):
   for c in range(TAMANHO_INTEIROS):
      if (x == inteiros[l][c]):
         xEstaNaMatriz = True
         print(f"'{x}' foi encontrado na posição {l + 1}x{c + 1}!")

if (not xEstaNaMatriz):
   print(f"'{x}' não foi encontrado!")
