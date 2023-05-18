'''
Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.
'''

inteiros = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

repeticoesPorInteiro = [[0, 0] for _ in range(len(inteiros))] # [inteiro, repetições]
repeticoesPorInteiro[0][0] = inteiros[0]
repeticoesPorInteiro[0][1] += 1
tamanhoRepeticoesPorInteiro = 1
inteiroMaisRepetido = repeticoesPorInteiro[0][0] # primeiro inteiro do vetor
repeticoesInteiroMaisRepetido = repeticoesPorInteiro[0][1] # repetições primeiro inteiro do vetor
for i in range(1, len(inteiros)):
   inteiroRegistrado = False
   for j in range(tamanhoRepeticoesPorInteiro):
      if (inteiros[i] == repeticoesPorInteiro[j][0]):
         repeticoesPorInteiro[j][1] += 1
         inteiroRegistrado = True
         break

   if (not inteiroRegistrado):
      repeticoesPorInteiro[tamanhoRepeticoesPorInteiro][0] = inteiros[i]
      repeticoesPorInteiro[tamanhoRepeticoesPorInteiro][1] += 1
      tamanhoRepeticoesPorInteiro += 1

   if (repeticoesPorInteiro[i][1] > repeticoesInteiroMaisRepetido):
      inteiroMaisRepetido = repeticoesPorInteiro[i][0]
      repeticoesInteiroMaisRepetido = repeticoesPorInteiro[i][1]

print(f"Inteiro que se repete mais vezes: {inteiroMaisRepetido}")
