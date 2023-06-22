from jogador import Computador, Humano
from console_colorido import ConsoleColorido

from time import sleep

class Jogo:
   def __init__(self, computador: Computador, humano: Humano):
      self._computador = computador
      self._humano = humano


   @property
   def computador(self) -> Computador:
      return self._computador


   @property
   def humano(self) -> Humano:
      return self._humano


   def _imprimirTabuleiros(self) -> None:
         print("\nTabuleiro do " + ConsoleColorido.textoNegritoAmarelo("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.computador.embarcacoes}\n")

         print("Tabuleiro do " + ConsoleColorido.textoNegritoAzul("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.humano.embarcacoes}\n")


   def executar(self) -> None:
      rodada = 1
      while ((self.computador.embarcacoes > 0) and (self.humano.embarcacoes > 0)):
         print(ConsoleColorido.textoNegrito("\n" + str(rodada) + "a RODADA"))
         rodada += 1

         print("Tabuleiro do " + ConsoleColorido.textoNegritoAmarelo("COMPUTADOR:"))
         self.computador.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.computador.embarcacoes}\n")
         sleep(1)
         self.humano.atacar(self.computador)
         sleep(2)

         print("Tabuleiro do " + ConsoleColorido.textoNegritoAzul("HUMANO:"))
         self.humano.tabuleiro.imprimir()
         print(f"Embarcações restantes: {self.humano.embarcacoes}\n")
         sleep(1)
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
