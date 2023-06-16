from console_colorido import ConsoleColorido
from tabuleiro import Tabuleiro

from abc import ABC, abstractmethod
import random
import re

class Jogador(ABC):
   def __init__(self, tabuleiro: Tabuleiro, embarcacoes: int):
      self._tabuleiro = tabuleiro
      self._embarcacoes = embarcacoes

      self._linhaColunaEmbarcacoes = set()


   @property
   def tabuleiro(self) -> Tabuleiro:
      return self._tabuleiro


   @property
   def embarcacoes(self) -> int:
      return self._embarcacoes


   @property
   def linhaColunaEmbarcacoes(self) -> set[tuple[int, int]]:
      return self._linhaColunaEmbarcacoes


   @abstractmethod
   def posicionarEmbarcacoes(self) -> None:
      pass



class Computador(Jogador):
   def posicionarEmbarcacoes(self) -> None:
      while (len(self.linhaColunaEmbarcacoes) < 5):
         linha = random.randrange(0, self.tabuleiro.linhas)
         coluna = random.randrange(0, self.tabuleiro.colunas)
         self.linhaColunaEmbarcacoes.add((linha, coluna))
      print(self.linhaColunaEmbarcacoes)



class Humano(Jogador):
   def _requisitarLinhaColuna(self) -> tuple[int, int]:
      REGEX_LINHA_COLUNA = r"\s*\d+\s+\d+\s*"
      while (not re.fullmatch(REGEX_LINHA_COLUNA,
                              linhaColuna := input("Digite a LINHA e a COLUNA (L C): "))):
         print(ConsoleColorido.textoVermelho("Entrada inválida!"))

      return tuple(int(x) for x in linhaColuna.split())


   def posicionarEmbarcacoes(self) -> None:
      tabuleiroTemporario = Tabuleiro(self.tabuleiro.linhas, self.tabuleiro.colunas)

      for i in range(self.embarcacoes):
         print()
         tabuleiroTemporario.imprimir()
         print()

         print(ConsoleColorido.textoNegritoAzul(f"Posicionando a {i + 1}a embarcação..."))
         while (not tabuleiroTemporario.posicionarEmbarcacao(linhaColuna := self._requisitarLinhaColuna())):
            print(ConsoleColorido.textoVermelho("Posição inválida!"))

         self.linhaColunaEmbarcacoes.add(linhaColuna)

      print()
      tabuleiroTemporario.imprimir()
      print()
