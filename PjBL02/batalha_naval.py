from jogo import Jogo
from jogador import Jogador
from tabuleiro import Tabuleiro

LINHAS = 5
COLUNAS = 10
EMBARCACOES = 5

computador = Jogador(Tabuleiro(LINHAS, COLUNAS, EMBARCACOES))
humano = Jogador(Tabuleiro(LINHAS, COLUNAS, EMBARCACOES))

jogo = Jogo(computador, humano)
jogo.executar()
