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


   def removerEmbarcacao(self, linhaColuna: tuple[int, int]) -> None:
      self.linhaColunaEmbarcacoes.remove(linhaColuna)
      self._embarcacoes -= 1


   def atacar(self, inimigo: "Jogador", linhaColuna: tuple[int, int]) -> None:
      linha, coluna = linhaColuna

      if (linhaColuna in inimigo.linhaColunaEmbarcacoes):
         inimigo.removerEmbarcacao(linhaColuna)
         print(ConsoleColorido.textoNegritoVermelho("Tiro certeiro!"))
         inimigo.tabuleiro[linha][coluna] = Tabuleiro.DESENHO_EMBARCACAO_ATINGIDA
      elif (inimigo.tabuleiro.em(linhaColuna) == Tabuleiro.DESENHO_EMBARCACAO_ATINGIDA):
         print(ConsoleColorido.textoNegritoAzul("A embarcação que estava aqui já naufragou!"))
      else:
         print(ConsoleColorido.textoNegritoAmarelo("Errroou!"))
         inimigo.tabuleiro[linha][coluna] = Tabuleiro.DESENHO_AGUA_ATINGIDA
      print()


   @abstractmethod
   def posicionarEmbarcacoes(self) -> None:
      pass



class Computador(Jogador):
   def _sortearPosicao(self) -> tuple[int, int]:
      linha = random.randrange(0, self.tabuleiro.linhas)
      coluna = random.randrange(0, self.tabuleiro.colunas)

      return (linha, coluna)


   def posicionarEmbarcacoes(self) -> None:
      while (len(self.linhaColunaEmbarcacoes) < self.embarcacoes):
         linhaColuna = self._sortearPosicao()
         self.linhaColunaEmbarcacoes.add(linhaColuna)


   def atacar(self, inimigo: Jogador) -> None:
      while ((linhaColuna := self._sortearPosicao()) and
             (inimigo.tabuleiro.em(linhaColuna) != Tabuleiro.DESENHO_AGUA)):
         pass

      linha, coluna = linhaColuna
      LINHA_COLORIDO = Tabuleiro.corIndiceLinha(str(linha))
      COLUNA_COLORIDO = Tabuleiro.corIndiceColuna(str(coluna))
      print(f"Computador escolheu {LINHA_COLORIDO} {COLUNA_COLORIDO}")

      super().atacar(inimigo, linhaColuna)



class Humano(Jogador):
   def _requisitarLinhaColuna(self) -> tuple[int, int]:
      REGEX_LINHA_COLUNA = r"\s*\d+\s+\d+\s*"
      L_COLORIDO = Tabuleiro.corIndiceLinha("L")
      C_COLORIDO = Tabuleiro.corIndiceColuna("C")
      while (not re.fullmatch(REGEX_LINHA_COLUNA,
                              linhaColuna := input(f"Digite a LINHA e a COLUNA ({L_COLORIDO} {C_COLORIDO}): "))):
         print(ConsoleColorido.textoVermelho("Entrada inválida!"))

      return tuple(int(x) for x in linhaColuna.split())


   def _posicionarEmbarcacao(self, tabuleiro: Tabuleiro, linhaColuna: tuple[int, int]) -> bool:
      if (not tabuleiro.posicaoValida(linhaColuna)):
         return False
      if (tabuleiro.em(linhaColuna) != Tabuleiro.DESENHO_AGUA):
         return False

      linha, coluna = linhaColuna
      tabuleiro[linha][coluna] = Tabuleiro.DESENHO_EMBARCACAO
      return True


   def posicionarEmbarcacoes(self) -> None:
      tabuleiroTemporario = Tabuleiro(self.tabuleiro.linhas, self.tabuleiro.colunas)

      for i in range(self.embarcacoes):
         print()
         tabuleiroTemporario.imprimir()
         print()

         print(f"Posicionando a {i + 1}a embarcação...")
         while ((linhaColuna := self._requisitarLinhaColuna()) and
                (not self._posicionarEmbarcacao(tabuleiroTemporario, linhaColuna))):
            print(ConsoleColorido.textoVermelho("Posição inválida!"))

         self.linhaColunaEmbarcacoes.add(linhaColuna)

      print()
      tabuleiroTemporario.imprimir()
      print()


   def atacar(self, inimigo: Jogador) -> None:
      while ((linhaColuna := self._requisitarLinhaColuna()) and
             (not inimigo.tabuleiro.posicaoValida(linhaColuna))):
         print(ConsoleColorido.textoVermelho("Posição inválida!"))

      super().atacar(inimigo, linhaColuna)
