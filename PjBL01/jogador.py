from jogadas import Jogadas
from abc import ABC, abstractmethod
import random

class Jogador(ABC):
   @abstractmethod
   def escolherJogada(self):
      pass

class Humano(Jogador):
   def escolherJogada(self):
      escolha = input("Qual sua escolha?\n"
                      "1 - Pedra\n"
                      "2 - Papel\n"
                      "3 - Tesoura\n")

      return escolha

class Computador(Jogador):
   def escolherJogada(self):
      return random.choice(list(Jogadas))