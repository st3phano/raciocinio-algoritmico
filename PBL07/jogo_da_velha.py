'''
Implemente um jogo da velha utilizando matrizes
'''

import re

def imprimirTabuleiro(tabuleiro: list) -> None:
   # imprime índice das colunas
   for i in range(len(tabuleiro[0])):
      print(f"  {i} ", end='')
   print()

   print(" ---" * 3)
   for iLinha in range(len(tabuleiro)):
      for iColuna in range(len(tabuleiro[iLinha])):
         print(f"| {tabuleiro[iLinha][iColuna]} ", end='')
      # imprime índice da linha
      print(f"| {iLinha}")
      print(" ---" * 3)

def requisitarLinhaColuna(linhasTabuleiro: int, colunasTabuleiro: int, pecaJogador: str) -> tuple[int, int]:
   SEPARADOR_REGEX_JOGADA = ' '
   REGEX_JOGADA = fr"[0-{linhasTabuleiro - 1}]{SEPARADOR_REGEX_JOGADA}[0-{colunasTabuleiro - 1}]"

   jogada = input(f"Jogador '{pecaJogador}' digite o índice da linha e da coluna desejada (L C): ")
   while (re.fullmatch(REGEX_JOGADA, jogada) == None):
      jogada = input("Por favor, digite índices válidos no formato 'L C': ")

   # converte a string de entrada em uma tupla (LINHA, COLUNA)
   return tuple(int(x) for x in jogada.split(SEPARADOR_REGEX_JOGADA))

def jogadaValida(tabuleiro: list, espacoVazio: str, linhaColuna: tuple[int, int]) -> bool:
   linha, coluna = linhaColuna
   return (tabuleiro[linha][coluna] == espacoVazio)


def requisitarJogada(tabuleiro: list, espacoVazio: str, pecaJogador: str) -> tuple[int, int]:
   LINHAS_TABULEIRO = len(tabuleiro)
   COLUNAS_TABULEIRO = len(tabuleiro[0])

   # recebe e valida uma jogada
   while (not jogadaValida(tabuleiro, espacoVazio,
          jogada := requisitarLinhaColuna(LINHAS_TABULEIRO, COLUNAS_TABULEIRO, pecaJogador))):
      print("Essa jogada é inválida!")

   return jogada

def ganhouNaLinha(linha: list, pecaJogador: str) -> bool:
   return all(x == pecaJogador for x in linha)

def ganhouNaColuna(tabuleiro: list, coluna: int, pecaJogador: str) -> bool:
   for linha in tabuleiro:
      if (linha[coluna] != pecaJogador):
         return False
   
   return True

def ganhouNaDiagonal(tabuleiro: list, linhaJogada: int, colunaJogada: int, pecaJogador: str) -> bool:
   LINHAS_TABULEIRO = len(tabuleiro)
   COLUNAS_TABULEIRO = len(tabuleiro[0])

   # jogada na diagonal?
   if (linhaJogada != colunaJogada):
      return False

   # checa diagonal primária e secundária
   linhaColuna = 0
   while (linhaColuna < LINHAS_TABULEIRO):
      linha = coluna = linhaColuna
      if ((tabuleiro[linha][coluna] != pecaJogador) or
          (tabuleiro[LINHAS_TABULEIRO - 1 - linha][COLUNAS_TABULEIRO - 1 - coluna] != pecaJogador)):
         return False
      linhaColuna += 1

   return True


def ganhouJogo(tabuleiro: list, jogada: tuple[int, int], pecaJogador: str) -> bool:
   LINHAS_TABULEIRO = len(tabuleiro)
   COLUNAS_TABULEIRO = len(tabuleiro[0])
   LINHA_JOGADA, COLUNA_JOGADA = jogada

   if (ganhouNaLinha(tabuleiro[LINHA_JOGADA], pecaJogador)):
      return True
   
   if (ganhouNaColuna(tabuleiro, COLUNA_JOGADA, pecaJogador)):
      return True
   
   if (ganhouNaDiagonal(tabuleiro, LINHA_JOGADA, COLUNA_JOGADA, pecaJogador)):
      return True

   return False



###############################################################################

LINHAS_TABULEIRO = 3
COLUNAS_TABULEIRO = 3
ESPACO_VAZIO_TABULEIRO = ' '
tabuleiro = [[ESPACO_VAZIO_TABULEIRO] * COLUNAS_TABULEIRO for _ in range(LINHAS_TABULEIRO)]

PECA_JOGADOR_1 = 'X'
PECA_JOGADOR_2 = 'O'
print("--- Jogo da Velha ---")
print(f"[-] Peça jogador 1: {PECA_JOGADOR_1}")
print(f"[-] Peça jogador 2: {PECA_JOGADOR_2}")
print()
imprimirTabuleiro(tabuleiro)
print()

acabou = False
while (not acabou):
   jogadaJogador1 = requisitarJogada(tabuleiro, ESPACO_VAZIO_TABULEIRO, PECA_JOGADOR_1)
   linha, coluna = jogadaJogador1
   tabuleiro[linha][coluna] = PECA_JOGADOR_1
   imprimirTabuleiro(tabuleiro)

   if (ganhouJogo(tabuleiro, jogadaJogador1, PECA_JOGADOR_1)):
      print("Jogador 1 GANHOU!")
      acabou = True

   if (not acabou):
      jogadaJogador2 = requisitarJogada(tabuleiro, ESPACO_VAZIO_TABULEIRO, PECA_JOGADOR_2)
      linha, coluna = jogadaJogador2
      tabuleiro[linha][coluna] = PECA_JOGADOR_2
      imprimirTabuleiro(tabuleiro)

      if (ganhouJogo(tabuleiro, jogadaJogador2, PECA_JOGADOR_2)):
         print("Jogador 2 GANHOU!")
         acabou = True
