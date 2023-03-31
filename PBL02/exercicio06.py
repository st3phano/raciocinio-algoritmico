'''
Faça um programa que peça um número inteiro entre 1 e 7 e informe o dia da semana correspondente
'''

numeroInt = int(input("Digite um número inteiro entre 1 e 7: "))

if (numeroInt == 1):
	print("Domingo")
elif (numeroInt == 2):
	print("Segunda")
elif (numeroInt == 3):
	print("Terça")
elif (numeroInt == 4):
	print("Quarta")
elif (numeroInt == 5):
	print("Quinta")
elif (numeroInt == 6):
	print("Sexta")
elif (numeroInt == 7):
	print("Sábado")
else:
	print("Número inválido")
