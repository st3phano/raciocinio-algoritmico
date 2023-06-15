'''
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida.
'''

def imprimirMatriz(matriz: list[list]) -> None:
   for linha in matriz:
      for coluna in linha:
         print(coluna, end='\t')
      print()

###################################################################################################

TAMANHO_INTEIROS = 5
inteiros = [[1 if (linha == coluna) else 0
             for coluna in range(TAMANHO_INTEIROS)]
            for linha in range(TAMANHO_INTEIROS)]

imprimirMatriz(inteiros)
