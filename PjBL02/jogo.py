from jogador import Jogador
from tabuleiro import Tabuleiro
from console_colorido import ConsoleColorido

from time import sleep
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


   def _imprimirTabuleiros(self) -> None:
         print("\nTabuleiro do " + ConsoleColorido.textoNegritoAmarelo("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.computador.embarcacoes}\n")

         print("Tabuleiro do " + ConsoleColorido.textoNegritoAzul("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.humano.embarcacoes}\n")


   def executar(self) -> None:
      while ((self.computador.embarcacoes > 0) and (self.humano.embarcacoes > 0)):
         print("\nTabuleiro do " + ConsoleColorido.textoNegritoAmarelo("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.computador.embarcacoes}\n")
         sleep(2)

         self.humano.atacar(self.computador)
         sleep(2)

         print("Tabuleiro do " + ConsoleColorido.textoNegritoAzul("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.humano.embarcacoes}\n")
         sleep(2)

         self.computador.atacar(self.humano)
         sleep(2)

      self._imprimirTabuleiros()
      sleep(2)
      if (self.computador.embarcacoes == 0):
         print("Parabéns! Você afundou todas as embarcações do inimigo!")
         if (self.humano.embarcacoes == 0):
            print("Porém também perdeu todas as suas embarcações...")
      else:
         print("Que pena, parece que você perdeu.")
