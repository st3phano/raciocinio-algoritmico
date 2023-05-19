'''
Escreva um programa que crie duas listas, uma com os números pares de 1 a 10
e outra com os números ímpares de 1 a 10. Em seguida, junte as duas listas em
uma terceira lista e a imprima na tela.
'''

NUMERO_MIN = 1
NUMERO_MAX = 10
pares = []
impares = []
for numero in range(NUMERO_MIN, NUMERO_MAX + 1):
   if (numero % 2 == 0):
      pares.append(numero)
   else:
      impares.append(numero)
print(pares)
print(impares)

paresImpares = pares + impares
print(paresImpares)
