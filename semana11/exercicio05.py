'''
Crie um vetor de 10 posições com números aleatórios.
Em seguida solicite ao usuário um número inteiro qualquer.
Verifique se o número digitado existe no vetor, então imprima:
a. Se o número existir: O número digitado foi X e existe na posição Y.
b. Se o número não existir: O número digitado foi X e não existe no vetor.
'''

import re
from random import randint

TAMANHO_INTEIROS_ALEATORIOS = 10
inteirosAleatorios = [0] * TAMANHO_INTEIROS_ALEATORIOS
INTEIRO_MIN = 1
INTEIRO_MAX = 100
for i in range(TAMANHO_INTEIROS_ALEATORIOS):
   inteirosAleatorios[i] = randint(INTEIRO_MIN, INTEIRO_MAX)
print(inteirosAleatorios)

REGEX_INTEIRO = r"[-+]?\d+"
inteiroQualquer = input("Digite um inteiro qualquer: ")
while (re.fullmatch(REGEX_INTEIRO, inteiroQualquer) == None):
   inteiroQualquer = input("Entrada inválida, digite um número inteiro: ")

inteiroQualquer = int(inteiroQualquer)
inteiroQualquerEncontrado = False
for i in range(TAMANHO_INTEIROS_ALEATORIOS):
   if (inteirosAleatorios[i] == inteiroQualquer):
      print(f"O número digitado foi {inteiroQualquer} e existe na posição {i}.")
      inteiroQualquerEncontrado = True

if (not inteiroQualquerEncontrado):
    print(f"O número digitado foi {inteiroQualquer} e não existe no vetor.")
