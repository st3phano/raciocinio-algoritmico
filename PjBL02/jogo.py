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


   def executar(self) -> None:
      vencedor = None
      while (vencedor == None):
         print("Tabuleiro do " + ConsoleColorido.negrito("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.negrito(self.computador.tabuleiro.embarcacoes)}\n")

         print("Tabuleiro do " + ConsoleColorido.negrito("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.negrito(self.humano.tabuleiro.embarcacoes)}\n")

         vencedor = 'a'

