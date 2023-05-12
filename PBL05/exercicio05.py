'''
Ler 10 números e imprimir quantos são pares e quantos são ímpares.
'''

import re

QUANTIDADE_INTEIROS = 10
inteiros = [0] * QUANTIDADE_INTEIROS
for i in range(QUANTIDADE_INTEIROS):
   inteiro = input(f"Digite o {i + 1}o número inteiro: ")

   REGEX_INTEIRO = r"[-+]?\d+"
   while (re.fullmatch(REGEX_INTEIRO, inteiro) == None):
      inteiro = input("Entrada inválida! Digite um número inteiro: ")

   inteiros[i] = int(inteiro)

quantidadePares = 0
quantidadeImpares = 0
for i in range(QUANTIDADE_INTEIROS):
   if (inteiros[i] % 2 == 0):
      quantidadePares += 1
   else:
      quantidadeImpares += 1
print(f"Foram digitados {quantidadePares} números pares e {quantidadeImpares} números impares.")
