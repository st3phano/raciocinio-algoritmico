'''
Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a
tabuada de 1 a 10 do valor lido.
'''

import re

REGEX_INTEIRO = r"[-+]?\d+"
INTEIRO_MIN = 1
INTEIRO_MAX = 10
inteiro = input("Digite um valor inteiro: ")
while ((re.fullmatch(REGEX_INTEIRO, inteiro) == None) or
       (int(inteiro) < INTEIRO_MIN or int(inteiro) > INTEIRO_MAX)):
   inteiro = input(f"Entrada inválida! Digite um inteiro entre {INTEIRO_MIN} e {INTEIRO_MAX}: ")

for i in range(1, 11):
   print(f"{inteiro} x {i} = {int(inteiro) * i}")
