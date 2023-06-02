from jogador import Jogador
from tabuleiro import Tabuleiro
from console_colorido import ConsoleColorido

import re

class Jogo:


   def __init__(self, computador: Jogador, humano: Jogador):
      self._computador = computador
      self._humano = humano


   @property
   def computador(self) -> Jogador:
      return self._computador


   @property
   def humano(self) -> Jogador:
      return self._humano


   def requisitarLinhaColuna(self) -> tuple[int, int]:
      linhaColuna = input("Entre com a linha e coluna desejada (L C): ")

      REGEX_LINHA_COLUNA = r"\s*\d+\s+\d+\s*"
      while (re.fullmatch(REGEX_LINHA_COLUNA, linhaColuna) == None):
         linhaColuna = input("Entrada inválida! Siga o formato (L C): ")

      return tuple(int(x) for x in linhaColuna.split())


   def executar(self) -> None:
      print(ConsoleColorido.textoNegrito("\n\t--- BATALHA NAVAL ---\n\n"))

      vencedor = None
      while (vencedor == None):
         print("Tabuleiro do " + ConsoleColorido.textoNegrito("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.textoNegrito(self.computador.tabuleiro.embarcacoes)}\n")

         print("Tabuleiro do " + ConsoleColorido.textoNegrito("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.textoNegrito(self.humano.tabuleiro.embarcacoes)}\n")

         vencedor = 'a'

