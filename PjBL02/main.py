'''
Batalha Naval é um jogo de tabuleiro de lápis e papel do qual participam dois jogadores. O objetivo do jogo
é afundar a tropa de navios do inimigo. Antes de iniciar o jogo, os jogadores posicionam a sua frota em seu
tabuleiro, sem revelar ao adversário tal posicionamento. As jogadas são feitas de forma alternada.
Quando da sua vez, o jogador “atira” em uma posição do tabuleiro do adversário indicando suas
coordenadas (linha e coluna). O jogo deve então informar se o tiro acertou algo ou não.
Ganha o jogo quem afundar primeiro a frota do adversário.
'''

from jogo import Jogo
from jogador import Computador
from jogador import Humano
from tabuleiro import Tabuleiro
from console_colorido import ConsoleColorido

from time import sleep

LINHAS = 5
COLUNAS = 10
EMBARCACOES = 5

print(ConsoleColorido.textoNegritoAzul("--- BATALHA NAVAL ---\n"))
sleep(1)

computador = Computador(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
computador.posicionarEmbarcacoes()

humano = Humano(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
print(ConsoleColorido.textoNegritoAmarelo("POSICIONE AS EMBARCAÇÕES:"))
sleep(1)
humano.posicionarEmbarcacoes()

jogo = Jogo(computador, humano)
print(ConsoleColorido.textoNegritoAmarelo("VAMOS INICIAR A BATALHA NAVAL!"))
sleep(1)
jogo.executar()
