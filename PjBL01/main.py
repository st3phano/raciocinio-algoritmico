from jogo import Jokenpo

'''
Implemente o jogo de jokenpô em python, de acordo com os requisitos abaixo:
1. O programa deve respeitar as regras do Jokenpô (Pedra ganha da tesoura / Tesoura ganha do papel
/ Papel ganha da pedra)
2. O jogo possui três modalidades: humano x humano, humano x computador ou computador x
computador. A escolha da modalidade deve ser definida no início do programa e não pode ser
modificada ao longo da execução.
3. Após a escolha da modalidade o jogo pode ter inúmeras partidas, ao final de cada partida o
programa deve perguntar se o jogador quer CONTINUAR ou SAIR.
4. Em cada partida o programa deve solicitar a jogada (PEDRA, PAPEL OU TESOURA) se o jogador for
humano ou gerar a jogada de forma randômica se o jogador for computador. Após coletar as
jogadas o programa deve indicar quem foi o vencedor e mostrar o placar geral.
5. Caso o jogador deseje CONTINUAR, o programa deve começar mais uma partida. Caso o jogador
deseje SAIR, o programa deve exibir o placar geral e apresentar uma mensagem de agradecimento.
'''

jokenpo = Jokenpo()
jokenpo.jogar()
