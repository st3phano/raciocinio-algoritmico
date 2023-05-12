'''
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''

somaPares = 0
QUANTIDADE_PARES = 50
for par in range(2, QUANTIDADE_PARES, 2):
   somaPares += par

print(f"A soma dos primeiros {QUANTIDADE_PARES} números pares é {somaPares}")
