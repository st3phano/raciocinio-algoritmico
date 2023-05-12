'''
Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.
'''

inteiros = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

inteiroMaisRepetido = 0
repeticoesInteiroMaisRepetido = 0
for i in range(len(inteiros)):
   inteiro = inteiros[i]
   repeticoesInteiro = 1
   for j in range(i + 1, len(inteiros)):
      if (inteiros[j] == inteiro):
         repeticoesInteiro += 1

   if (repeticoesInteiro > repeticoesInteiroMaisRepetido):
      repeticoesInteiroMaisRepetido = repeticoesInteiro
      inteiroMaisRepetido = inteiro

print(f"Inteiro que se repete mais vezes: {inteiroMaisRepetido}")
