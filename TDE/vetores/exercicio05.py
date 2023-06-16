'''
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
'''

import re

def lerNumeroInteiro(requisicao: str) -> int:
   REGEX_INTEIRO = r"[-+]?\d+"

   while (not re.fullmatch(REGEX_INTEIRO,
                           inteiro := input(requisicao))):
      print(f"'{inteiro}' não é um número inteiro!")

   return int(inteiro)

def contarNumerosInteirosPar(inteiros: list[int]) -> int:
   pares = 0
   for inteiro in inteiros:
      if (inteiro % 2 == 0):
         pares += 1

   return pares

###################################################################################################

TAMANHO_INTEIROS = 10
inteiros = list()
for i in range(TAMANHO_INTEIROS):
   inteiros.append(lerNumeroInteiro(f"Digite o {i + 1}o número inteiro: "))

pares = contarNumerosInteirosPar(inteiros)
print(f"Foram digitados {pares} números inteiros par!")
