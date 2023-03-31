'''
Faça um programa que peça a idade de uma pessoa e informe se ela pode votar ou não
'''

idadePessoa = int(print("Digite sua idade: "))

IDADE_MINIMA_VOTAR = 16
if (idadePessoa < IDADE_MINIMA_VOTAR):
	print("Você não pode votar")
else:
	print("Você pode votar")
