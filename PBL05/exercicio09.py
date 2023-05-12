'''
Faça um algoritmo que leia 10 números inteiros,
armazene-os em uma lista e imprima em ordem crescente.
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

inteirosCrescente = inteiros
for i in range(QUANTIDADE_INTEIROS - 1):
   for j in range(i + 1, QUANTIDADE_INTEIROS):
      if (inteirosCrescente[j] < inteirosCrescente[i]):
         aux = inteirosCrescente[i]
         inteirosCrescente[i] = inteirosCrescente[j]
         inteirosCrescente[j] = aux
print(inteirosCrescente)
