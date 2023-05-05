'''
Faça um programa que preenche um vetor com valores inteiros até que
o usuário digite um valor negativo (o valor negativo não deve ser
inserido no vetor). Imprima:
a. O vetor.
b. A quantidade de valores maiores que 5.
c. A soma dos valores pares armazenados no vetor.
d. A soma dos valores ímpares armazenados no vetor.
e. A quantidade total de valores armazenados no vetor.
'''

CAPACIDADE_VALORES_INTEIROS = 100
valoresInteiros = [0] * CAPACIDADE_VALORES_INTEIROS
print("Digite valores inteiros (valor negativo encerra a entrada)")
tamanhoValoresInteiros = 0
while (tamanhoValoresInteiros < CAPACIDADE_VALORES_INTEIROS and (valorInteiro := input(": ")).isdecimal()):
   valoresInteiros[tamanhoValoresInteiros] = int(valorInteiro)
   tamanhoValoresInteiros += 1

# Imprima o vetor.
for i in range(tamanhoValoresInteiros):
   print(valoresInteiros[i], end=' ')
print()

# Imprima a quantidade de valores maiores que 5
maioresQue5 = 0
for i in range(tamanhoValoresInteiros):
   if (valoresInteiros[i] > 5):
      maioresQue5 += 1
print(f"Valores maiores que 5: {maioresQue5}")

# A soma dos valores pares armazenados no vetor.
# A soma dos valores ímpares armazenados no vetor.
somaPares = 0
somaImpares = 0
for i in range(tamanhoValoresInteiros):
   if (valoresInteiros[i] % 2 == 0):
      somaPares += valoresInteiros[i]
   else:
      somaImpares += valoresInteiros[i]
print(f"A soma dos valores pares é {somaPares} e a soma dos valores ímpares é {somaImpares}")

# A quantidade total de valores armazenados no vetor.
print(f"O vetor possui {tamanhoValoresInteiros} elementos")
