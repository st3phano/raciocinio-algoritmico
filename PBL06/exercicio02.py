'''
Escreva um programa que peça ao usuário três números e os armazene em uma
lista. Em seguida, imprima a lista na tela.
'''

import re

numeros = []
TAMANHO_NUMEROS = 3
for i in range(TAMANHO_NUMEROS):
   numero = input(f"Digite o {i + 1} número da lista: ")

   REGEX_REAL = r"[-+]?\d*\.?\d+"
   while (re.fullmatch(REGEX_REAL, numero) == None):
      numero = input(f"Por favor digite um número real: ")

   numeros.append(float(numero))

print(numeros)
