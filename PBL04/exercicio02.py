'''
Faça um programa que preenche um vetor de 50 posições com valores
aleatórios entre 0 e 20 e encontre:
a. A soma dos valores armazenados no vetor.
b. O número de ocorrências do valor 9.
c. O maior valor armazenado no vetor.
d. O menor valor armazenado no vetor.
'''

from random import randint

TAMANHO_VALORES_ALEATORIOS = 50
MIN_VALOR_ALEATORIO = 0
MAX_VALOR_ALEATORIO = 20
valoresAleatorios = [0] * TAMANHO_VALORES_ALEATORIOS
for i in range(TAMANHO_VALORES_ALEATORIOS):
   valoresAleatorios[i] = randint(MIN_VALOR_ALEATORIO, MAX_VALOR_ALEATORIO)
print(valoresAleatorios)

# A soma dos valores armazenados no vetor.
somaValoresAleatorios = 0
for valor in valoresAleatorios:
   somaValoresAleatorios += valor
print(f"Soma dos valores do vetor: {somaValoresAleatorios}")

# O número de ocorrências do valor 9.
ocorrenciasValor9 = valoresAleatorios.count(9)

# O maior valor armazenado no vetor.
# O menor valor armazenado no vetor.
menorValor = maiorValor = valoresAleatorios[0]
for i in range(1, TAMANHO_VALORES_ALEATORIOS):
   if (valoresAleatorios[i] > maiorValor):
      maiorValor = valoresAleatorios[i]
   elif (valoresAleatorios[i] < menorValor):
      menorValor = valoresAleatorios[i]
print(f"Maior valor armazenado no vetor: {maiorValor}")
print(f"Menor valor armazenado no vetor: {menorValor}")
