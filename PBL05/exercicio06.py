'''
Utilizando a estrutura de repetição for, faça um programa que receba 10
números e conte quantos deles estão no intervalo [10,20] e quantos deles
estão fora do intervalo.
'''

import re

quantidadeNoIntervalo = 0
LIMITE_INFERIOR_INTERVALO = 10
LIMITE_SUPERIOR_INTERVALO = 20
QUANTIDADE_INTEIROS = 10
for i in range(QUANTIDADE_INTEIROS):
   inteiro = input(f"Digite o {i + 1} número inteiro: ")

   REGEX_INTEIRO = r"[-+]?\d+"
   while (re.fullmatch(REGEX_INTEIRO, inteiro) == None):
      inteiro = input(f"Entrada inválida! Digite um número inteiro: ")

   if (LIMITE_INFERIOR_INTERVALO <= int(inteiro) <= LIMITE_SUPERIOR_INTERVALO):
      quantidadeNoIntervalo += 1

quantidadeForaDoIntervalo = QUANTIDADE_INTEIROS - quantidadeNoIntervalo
print(f"{quantidadeNoIntervalo} números estão no intervalo de {LIMITE_INFERIOR_INTERVALO} e {LIMITE_SUPERIOR_INTERVALO}\n"
      f"{quantidadeForaDoIntervalo} estão fora desse intervalo")
