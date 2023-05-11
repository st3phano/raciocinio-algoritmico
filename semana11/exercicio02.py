'''
Imprimir os elementos de um vetor qualquer
'''

from random import sample

vetor = sample(range(100), 10)
for elemento in vetor:
   print(f"[{elemento}]", end=' ')
print()
