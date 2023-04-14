from jogador import Humano
from jogador import Computador

from enum import Enum
from time import sleep


class ModalidadesJogo(Enum):
   HUMANOvsHUMANO = '1'
   HUMANOvsCOMPUTADOR = '2'
   COMPUTADORvsCOMPUTADOR = '3'


   @staticmethod
   def imprimirModalidades():
      for modalidade in ModalidadesJogo:
         print(f"{modalidade.value} - {modalidade.name}")


class Jogo:
   def escolherModalidade(self):
      print("Qual modalidade deseja jogar?")
      ModalidadesJogo.imprimirModalidades()
      modalidade = input(": ")

      while (modalidade not in [m.value for m in ModalidadesJogo]):
         modalidade = input("Modalidade inválida! Escolha uma entre as modalidades disponíveis: ")

      return ModalidadesJogo(modalidade)


   def definirVencedor(self, jogador1, jogador2):
      jogada1 = int(jogador1.jogada.value)
      jogada2 = int(jogador2.jogada.value)

      if (jogada1 == jogada2):
         return 0
      elif ((jogada1 == jogada2 + 1) or (jogada1 == jogada2 - 2)):
         return 1
      else:
         return 2


   def jogarPartida(self, numeroPartida, jogador1, jogador2):
      print(f"Partida {numeroPartida} de Jokenpo:\n")
      sleep(1)

      print(" - Vez do jogador 1 -")
      sleep(1)
      jogador1.escolherJogada()
      print(f"Jogador 1 escolheu {jogador1.jogada.name}")
      sleep(1)

      print(" - Vez do jogador 2 -")
      sleep(1)
      jogador2.escolherJogada()
      print(f"Jogador 2 escolheu {jogador2.jogada.name}")
      sleep(1)

      vencedor = self.definirVencedor(jogador1, jogador2)
      if (vencedor == 1):
         print(" - Jogador 1 venceu! -")
         jogador1.numeroVitorias += 1
      elif (vencedor == 2):
         print(" - Jogador 2 venceu! -")
         jogador2.numeroVitorias += 1
      else:
         print(" - Empate! -")
      sleep(1)


   def jogar(self):
      modalidade = self.escolherModalidade()

      if (modalidade == ModalidadesJogo.HUMANOvsHUMANO):
         jogador1 = Humano()
         jogador2 = Humano()
      elif (modalidade == ModalidadesJogo.HUMANOvsCOMPUTADOR):
         jogador1 = Humano()
         jogador2 = Computador()
      else: # ModalidadesDeJogo.COMPUTADORvsCOMPUTADOR
         jogador1 = Computador()
         jogador2 = Computador()

      numeroPartida = 0
      continuarJogando = '1'
      while (continuarJogando != '0'):
         numeroPartida += 1
         self.jogarPartida(numeroPartida, jogador1, jogador2)
         continuarJogando = input("Deseja jogar mais uma partida? (0 - não / 1 - sim)\n: ")
         print()
         sleep(1)

      print(f"Jogador 1 venceu {jogador1.numeroVitorias} partidas!")
      sleep(1)
      print(f"Jogador 2 venceu {jogador2.numeroVitorias} partidas!")
