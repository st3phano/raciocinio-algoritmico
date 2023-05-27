'''
Implemente um jogo da velha utilizando matrizes
'''

import re

def imprimirTabuleiro(tabuleiro: list, tamanhoTabuleiro: int) -> None:
   print()
   # imprime índices das colunas
   for iColuna in range(tamanhoTabuleiro):
      if (iColuna < 10):
         coluna = f"  {iColuna} "
      else:
         coluna = f"  {iColuna}"
      print(coluna, end='')
   print()

   print(" ---" * tamanhoTabuleiro)
   for iLinha in range(tamanhoTabuleiro):
      for coluna in tabuleiro[iLinha]:
         print(f"| {coluna} ", end='')
      print(f"| {iLinha}") # imprime índice da linha
      print(" ---" * tamanhoTabuleiro)
   print()


def requisitarLinhaColuna(pecaJogador: str) -> tuple[int, int]:
   REGEX_JOGADA = r"\s*\d+\s+\d+\s*"

   jogada = input(f"Jogador '{pecaJogador}' digite os índices da linha e da coluna desejados (L C): ")
   while (re.fullmatch(REGEX_JOGADA, jogada) == None):
      jogada = input("Por favor, digite índices no formato (L C): ")

   # converte a string digitada em tupla(LINHA, COLUNA)
   return tuple(int(x) for x in jogada.split())


def linhaColunaValida(tabuleiro: list, tamanhoTabuleiro: int, espacoVazio: str, linhaColuna: tuple[int, int]) -> bool:
   LINHA, COLUNA = linhaColuna

   return (LINHA < tamanhoTabuleiro) and (COLUNA < tamanhoTabuleiro) and (tabuleiro[LINHA][COLUNA] == espacoVazio)


def requisitarJogada(tabuleiro: list, tamanhoTabuleiro: int, espacoVazio: str, pecaJogador: str) -> tuple[int, int]:
   while (not linhaColunaValida(tabuleiro, tamanhoTabuleiro, espacoVazio,
          jogada := requisitarLinhaColuna(pecaJogador))):
      print("Jogada inválida!")

   return jogada


def ganhouNaLinha(linha: list, pecaJogador: str) -> bool:
   return all((x == pecaJogador) for x in linha)


def ganhouNaColuna(tabuleiro: list, coluna: int, pecaJogador: str) -> bool:
   return all((linha[coluna] == pecaJogador) for linha in tabuleiro)


def ganhouNaDiagonal(tabuleiro: list, tamanhoTabuleiro: int, pecaJogador: str) -> bool:
   return ((all((tabuleiro[x][x] == pecaJogador)
               for x in range(tamanhoTabuleiro))) or
           (all((tabuleiro[x][tamanhoTabuleiro - 1 - x] == pecaJogador)
               for x in range(tamanhoTabuleiro))))


def ganhouJogo(tabuleiro: list, tamanhoTabuleiro: int, jogada: tuple[int, int], pecaJogador: str) -> bool:
   LINHA_JOGADA, COLUNA_JOGADA = jogada

   if (ganhouNaLinha(tabuleiro[LINHA_JOGADA], pecaJogador)):
      return True
   
   if (ganhouNaColuna(tabuleiro, COLUNA_JOGADA, pecaJogador)):
      return True
   
   if (ganhouNaDiagonal(tabuleiro, tamanhoTabuleiro, pecaJogador)):
      return True

   return False

###################################################################################################

TAMANHO_TABULEIRO = 6
ESPACO_VAZIO = ' '
tabuleiro = [[ESPACO_VAZIO] * TAMANHO_TABULEIRO for _ in range(TAMANHO_TABULEIRO)]

PECA_JOGADORES = ('X', 'O', 'Y')
NUMERO_JOGADORES = len(PECA_JOGADORES)
print("--- Jogo da Velha ---")
for i in range(NUMERO_JOGADORES):
   print(f"[-] Peça jogador {i + 1}: {PECA_JOGADORES[i]}")
imprimirTabuleiro(tabuleiro, TAMANHO_TABULEIRO)

jogador = 0
jogadorGanhador = -1
espacosRestantes = TAMANHO_TABULEIRO ** 2
while ((jogadorGanhador == -1) and (espacosRestantes > 0)):
   jogada = requisitarJogada(tabuleiro, TAMANHO_TABULEIRO, ESPACO_VAZIO, PECA_JOGADORES[jogador])
   linha, coluna = jogada
   tabuleiro[linha][coluna] = PECA_JOGADORES[jogador]
   espacosRestantes -= 1

   imprimirTabuleiro(tabuleiro, TAMANHO_TABULEIRO)

   if (ganhouJogo(tabuleiro, TAMANHO_TABULEIRO, jogada, PECA_JOGADORES[jogador])):
      jogadorGanhador = jogador
   elif (jogador + 1 == NUMERO_JOGADORES):
      jogador = 0
   else:
      jogador += 1

if (jogadorGanhador == -1):
   print("Empate!")
else:
   print(f"O jogador '{PECA_JOGADORES[jogadorGanhador]}' ganhou!")
