'''
Crie um programa em Python para um jogo de RPG que permita que o
jogador escolha um personagem. As opções são: guerreiro, mago e
arqueiro. O programa deve definir a vida para cada personagem de acordo
com a tabela abaixo. Se o jogador escolher um personagem inválido, o
programa deve apresentar uma mensagem de erro. Ao final, o programa
deve imprimir qual personagem foi escolhido e sua respectiva vida.

Personagem   Vida
Guerreiro    200
Mago         130
Arqueiro     100
'''

personagemVida = {"guerreiro": 200, "mago": 130, "arqueiro": 100}

print("Escolha seu personagem:")
for personagem in personagemVida:
   print(f"- {personagem}")
while (escolha := input(": ")) not in personagemVida:
   print("Escolha inválida, tente novamente!")

print(f"{escolha}s possuem {personagemVida[escolha]} pontos de vida!")
