'''
Faça um programa que leia um vetor de 10 posições e verifique se
existem valores iguais e os escreva na tela.
'''

TAMANHO_VALORES = 10
valores = [None] * TAMANHO_VALORES
for i in range(TAMANHO_VALORES):
   valores[i] = input(f"Digite o {i + 1}o elemento:\t")

valoresVistos = [None] * TAMANHO_VALORES
iVistos = 0
valoresRepetidos = [None] * TAMANHO_VALORES
iRepetidos = 0
for i in range(TAMANHO_VALORES):
   if (valores[i] not in valoresVistos):
      valoresVistos[iVistos] = valores[i]
      iVistos += 1
   else:
      valoresRepetidos[iRepetidos] = valores[i]
      iRepetidos += 1

print("Valores repetidos:", end=' ')
for i in range(iRepetidos):
   print(valoresRepetidos[i], end=' ')
print()
