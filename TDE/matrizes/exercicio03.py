'''
Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e da
coluna de cada elemento. Em seguida, imprima na tela a matriz.
'''

def imprimirMatriz(matriz: list[list]) -> None:
   for linha in matriz:
      for coluna in linha:
         print(coluna, end='\t')
      print()

###################################################################################################

TAMANHO_INTEIROS = 4
inteiros = [[(linha + 1) * (coluna + 1)
             for coluna in range(TAMANHO_INTEIROS)]
            for linha in range(TAMANHO_INTEIROS)]

imprimirMatriz(inteiros)
