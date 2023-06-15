'''
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
'''

import re

def lerNumeroReal(requisicao: str) -> float:
   REGEX_REAL = r"[-+]?\d*\.?\d+"

   while (not re.fullmatch(REGEX_REAL,
                           real := input(requisicao))):
      print(f"'{real}' não é um número real!")

   return float(real)

def contarOcorrencias(lista: list, funcaoOcorrencia) -> int:
   ocorrencias = 0
   for elemento in lista:
      if (funcaoOcorrencia(elemento)):
         ocorrencias += 1

   return ocorrencias

###################################################################################################

TAMANHO_REAIS = 4
reais = [[lerNumeroReal(f"Digite um número real para posição {linha + 1}x{coluna + 1}: ")
           for coluna in range(TAMANHO_REAIS)]
          for linha in range(TAMANHO_REAIS)]

X = 10
maioresQueX = 0
for linha in reais:
   maioresQueX += contarOcorrencias(linha, lambda real: real > X)
print(f"Foram digitados {maioresQueX} números maiores que {X}")
