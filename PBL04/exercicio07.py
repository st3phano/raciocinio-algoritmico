'''
Faça um programa que leia um vetor de 15 posições e o compacte, ou
seja, elimine as posições com valor zero. Para isso, todos os elementos
a frente do valor zero, devem ser movidos uma posição para trás no
vetor.
'''

import re

tamanhoValores = 15
valores = [0] * tamanhoValores
for iValores in range(tamanhoValores):
   valorDigitado = input(f"Digite o {iValores + 1}o valor: ")
   
   regexNumeroReal = r"[-+]?\d*\.?\d+?"
   while (re.fullmatch(regexNumeroReal, valorDigitado) == None):
      valorDigitado = input("Entrada inválida! Digite um valor real: ")

   valores[iValores] = float(valorDigitado)

iValores = 0
while (iValores < tamanhoValores):
   if (valores[iValores] == 0):
      j = iValores + 1
      while (j < tamanhoValores):
         valores[j - 1] = valores[j]
         j += 1
      tamanhoValores -= 1
   else:
      iValores += 1

print("Valores compactado:", end=' ')
for i in range(tamanhoValores):
   print(valores[i], end=' ')
print()
