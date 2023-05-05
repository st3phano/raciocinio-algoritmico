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
   valores[iValores] = input(f"Digite o {iValores + 1}o valor: ")

zeroRegex = r"0+"
iValores = 0
while (iValores < tamanhoValores):
   if (re.match(zeroRegex, valores[iValores])):
      j = iValores + 1
      while (j < tamanhoValores):
         valores[j - 1] = valores[j]
         j += 1
      tamanhoValores -= 1
   else:
      iValores += 1

print("Valores compactado:", end=' ')
for i in range(tamanhoValores):
   print(valores[i],end=' ')
print()
