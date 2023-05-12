'''
Dado um vetor A de tamanho N e um vetor B de tamanho N, crie um programa
que calcule a soma dos elementos desses vetores e armazene o resultado em
um vetor C de tamanho N. Regras:
a. O tamanho dos vetores A, B e C é fornecido pelo usuário.
b. Os elementos dos vetores A e B são fornecidos pelo usuário.
c. A soma dos elementos de A[i] e B[i] deve ser armazenada em C[i].
d. O vetor C deve ser exibido na tela após o cálculo.
'''

import re

tamanhoVetores = input("Digite o tamanho dos vetores: ")
while (not tamanhoVetores.isdecimal()):
   tamanhoVetores = input("Tamanho inválido! Tente novamente: ")
tamanhoVetores = int(tamanhoVetores)

QUANTIDADE_VETORES = 2
vetores = [[0] * tamanhoVetores] * QUANTIDADE_VETORES
vetorSoma = [0] * tamanhoVetores
for numeroVetor in range(QUANTIDADE_VETORES):
   for i in range(tamanhoVetores):
      numeroReal = input(f"Digite o {i + 1}o número do {numeroVetor + 1}o vetor: ")

      REGEX_FLOAT = r"[-+]?\d*\.?\d+"
      while (re.fullmatch(REGEX_FLOAT, numeroReal) == None):
         numeroReal = input("Número inválido! Digite um número com ou sem ponto flutuante: ")

      numeroReal = float(numeroReal)
      vetores[numeroVetor][i] = numeroReal
      vetorSoma[i] += numeroReal

print(vetorSoma)
