'''
Fazer um programa para encontrar todos os números pares entre 1 e 100.
'''

INTEIRO_MIN = 1
INTEIRO_MAX = 100
pares = [0] * ((INTEIRO_MAX - INTEIRO_MIN) + 1)

i = 0
for inteiro in range(INTEIRO_MIN, INTEIRO_MAX + 1):
   if (inteiro % 2 == 0):
      pares[i] = inteiro
      i += 1
print(pares[:i])
