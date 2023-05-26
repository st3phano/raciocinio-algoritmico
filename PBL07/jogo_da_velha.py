'''
Implemente um jogo da velha utilizando matrizes
'''

import re

def imprimirTabuleiro(tabuleiro: list, tamanhoTabuleiro: int) -> None:
   print()
   # imprime índices das colunas
   for iColuna in range(tamanhoTabuleiro):
      print(f"  {iColuna} ", end='')
   print()

   print(" ---" * tamanhoTabuleiro)
   for iLinha in range(tamanhoTabuleiro):
      for coluna in tabuleiro[iLinha]:
         print(f"| {coluna} ", end='')
      print(f"| {iLinha}") # imprime índice da linha
      print(" ---" * tamanhoTabuleiro)
   print()


def requisitarLinhaColuna(tamanhoTabuleiro: int, pecaJogador: str) -> tuple[int, int]:
   REGEX_JOGADA = fr"\s*[0-{tamanhoTabuleiro - 1}]\s+[0-{tamanhoTabuleiro - 1}]\s*"

   jogada = input(f"Jogador '{pecaJogador}' digite o índice da linha e da coluna desejados (L C): ")
   while (re.fullmatch(REGEX_JOGADA, jogada) == None):
      jogada = input("Por favor, digite índices válidos no formato 'L C': ")

   # converte a string digitada em tupla(LINHA, COLUNA)
   return tuple(int(x) for x in jogada.split())


def linhaColunaValida(tabuleiro: list, espacoVazio: str, linhaColuna: tuple[int, int]) -> bool:
   linha, coluna = linhaColuna
   return (tabuleiro[linha][coluna] == espacoVazio)


def requisitarJogada(tabuleiro: list, tamanhoTabuleiro: int, espacoVazio: str, pecaJogador: str) -> tuple[int, int]:
   while (not linhaColunaValida(tabuleiro, espacoVazio,
          jogada := requisitarLinhaColuna(tamanhoTabuleiro, pecaJogador))):
      print("Essa jogada é inválida!")

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


###############################################################################


TAMANHO_TABULEIRO = 4
ESPACO_VAZIO = ' '
tabuleiro = [[ESPACO_VAZIO] * TAMANHO_TABULEIRO for _ in range(TAMANHO_TABULEIRO)]

PECA_JOGADORES = ('X', 'O')
print("--- Jogo da Velha ---")
for i in range(len(PECA_JOGADORES)):
   print(f"[-] Peça jogador {i + 1}: {PECA_JOGADORES[i]}")
imprimirTabuleiro(tabuleiro, TAMANHO_TABULEIRO)

jogadorGanhador = -1
while (jogadorGanhador == -1):
   jogadas = [None] * len(PECA_JOGADORES)

   for jogador in range(len(PECA_JOGADORES)):
      jogadas[jogador] = requisitarJogada(tabuleiro, TAMANHO_TABULEIRO, ESPACO_VAZIO, PECA_JOGADORES[jogador])
      linha, coluna = jogadas[jogador]
      tabuleiro[linha][coluna] = PECA_JOGADORES[jogador]
      imprimirTabuleiro(tabuleiro, TAMANHO_TABULEIRO)

      if (ganhouJogo(tabuleiro, TAMANHO_TABULEIRO, jogadas[jogador], PECA_JOGADORES[jogador])):
         jogadorGanhador = jogador
         break

print(f"O jogador '{PECA_JOGADORES[jogadorGanhador]}' ganhou o jogo!")
