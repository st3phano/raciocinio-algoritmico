from enum import Enum
from abc import ABC, abstractmethod
from random import choice


class Jogadas(Enum):
   PEDRA = '1'
   PAPEL = '2'
   TESOURA = '3'


   @staticmethod
   def imprimirJogadas():
      for jogada in Jogadas:
         print(f"{jogada.value} - {jogada.name}")


class Jogador(ABC):
   def __init__(self):
      self._numeroVitorias = 0


   @property
   def jogada(self):
      return self._jogada
   @jogada.setter
   def jogada(self, jogada):
      if (jogada in Jogadas):
         self._jogada = jogada


   @property
   def numeroVitorias(self):
      return self._numeroVitorias
   @numeroVitorias.setter
   def numeroVitorias(self, numeroVitorias):
      self._numeroVitorias = numeroVitorias


   @abstractmethod
   def escolherJogada(self):
      pass


class Humano(Jogador):
   def escolherJogada(self):
      print("Qual sua jogada?")
      Jogadas.imprimirJogadas()
      jogada = input(": ")

      while (jogada not in [j.value for j in Jogadas]):
         jogada = input("Jogada inválida! Escolha uma entre as jogadas disponíveis: ")

      self.jogada = Jogadas(jogada)


class Computador(Jogador):
   def escolherJogada(self):
      self.jogada = choice(list(Jogadas))