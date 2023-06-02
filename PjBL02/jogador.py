from console_colorido import ConsoleColorido
from tabuleiro import Tabuleiro

import re

class Jogador:
   def __init__(self, tabuleiro: Tabuleiro, embarcacoes: int):
      self._tabuleiro = tabuleiro
      self._embarcacoes = embarcacoes

      self._linhaColunaEmbarcacoes = [None] * embarcacoes


   @property
   def tabuleiro(self) -> Tabuleiro:
      return self._tabuleiro


   @property
   def embarcacoes(self) -> int:
      return self._embarcacoes


   @property
   def linhaColunaEmbarcacoes(self) -> list[tuple[int, int]]:
      return self._linhaColunaEmbarcacoes


   def posicionarEmbarcacoes(self) -> None:
      pass



class Computador(Jogador):
   pass



class Humano(Jogador):
   def _posicionarEmbarcacao(self, linhaColuna: tuple[int, int]) -> bool:
      linha, coluna = linhaColuna
      LINHAS = self.tabuleiro.linhas
      COLUNAS = self.tabuleiro.colunas
      if ((linha < 0 or linha >= LINHAS) or (coluna < 0 or coluna >= COLUNAS)):
         return False

      if (self.tabuleiro[linha][coluna] != Tabuleiro.CARACTERE_AGUA):
         return False

      self.tabuleiro[linha][coluna] = Tabuleiro.CARACTERE_EMBARCACAO
      return True


   def _requisitarLinhaColuna(self) -> tuple[int, int]:
      linhaColuna = input("Digite a LINHA e a COLUNA (L C): ")

      REGEX_LINHA_COLUNA = r"\s*\d+\s+\d+\s*"
      while (re.fullmatch(REGEX_LINHA_COLUNA, linhaColuna) == None):
         linhaColuna = input("Entrada inválida! Siga o formato (L C): ")

      return tuple(int(x) for x in linhaColuna.split())


   def posicionarEmbarcacoes(self) -> None:
      print(ConsoleColorido.negrito("\n--- BATALHA NAVAL ---\n"))

      for i in range(len(self.linhaColunaEmbarcacoes)):
         print(f"\nPosicionando a {ConsoleColorido.negrito(str(i + 1) + 'a')} embarcação...\n")
         self.tabuleiro.imprimir()
         print()

         while (not self._posicionarEmbarcacao(
                    self._requisitarLinhaColuna())):
            print("Posição inválida!")




