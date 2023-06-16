from jogo import Jogo
from jogador import Computador
from jogador import Humano
from tabuleiro import Tabuleiro
from console_colorido import ConsoleColorido

LINHAS = 5
COLUNAS = 10
EMBARCACOES = 5

print(ConsoleColorido.textoNegritoAzul("--- BATALHA NAVAL ---\n"))

computador = Computador(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
computador.posicionarEmbarcacoes()

humano = Humano(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
print(ConsoleColorido.textoNegritoAmarelo("POSICIONE AS EMBARCAÇÕES:"))
humano.posicionarEmbarcacoes()

jogo = Jogo(computador, humano)
print(ConsoleColorido.textoNegritoAmarelo("VAMOS INICIAR A BATALHA NAVAL!"))
jogo.executar()
