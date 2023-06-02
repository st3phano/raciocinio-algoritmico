from tabuleiro import Tabuleiro

class Jogador:
   def __init__(self, tabuleiro: Tabuleiro):
      self._tabuleiro = tabuleiro


   @property
   def tabuleiro(self) -> Tabuleiro:
      return self._tabuleiro

