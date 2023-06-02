from jogo import Jogo
from jogador import Jogador
from jogador import Computador
from jogador import Humano
from tabuleiro import Tabuleiro

LINHAS = 5
COLUNAS = 10
EMBARCACOES = 5

computador = Jogador(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
humano = Humano(Tabuleiro(LINHAS, COLUNAS), EMBARCACOES)
humano.posicionarEmbarcacoes()

jogo = Jogo(computador, humano)
jogo.executar()
