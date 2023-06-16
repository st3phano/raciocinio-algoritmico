from jogo import Jogo
from jogador import Computador
from jogador import Humano
from tabuleiro import Tabuleiro
from console_colorido import ConsoleColorido

from time import sleep

LINHAS = 3
COLUNAS = 3
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
