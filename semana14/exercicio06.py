'''
Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.
'''

def imprimirDiagonal(matriz: list[list[float]]) -> None:
   LINHAS = len(matriz)
   if (LINHAS == 0):
      return

   COLUNAS = len(matriz[0])
   if ((COLUNAS == 0) or (LINHAS != COLUNAS)):
      return

   for i in range(LINHAS):
      print(matriz[i][i], end=' ')
   print()

from random import randint

TAMANHO_MATRIZ = 3
matriz = [[randint(linha - 10, coluna + 10)
           for coluna in range(TAMANHO_MATRIZ)]
          for linha in range(TAMANHO_MATRIZ)]

imprimirDiagonal(matriz)
