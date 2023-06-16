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
         print("\nTabuleiro do " + ConsoleColorido.textoNegritoVermelho("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.textoNegritoAmarelo(str(self.computador.embarcacoes))}\n")

         print("\nTabuleiro do " + ConsoleColorido.textoNegritoAzul("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print("Embarcações restantes: "
               f"{ConsoleColorido.textoNegritoAmarelo(str(self.humano.embarcacoes))}\n")

         vencedor = 'a'

