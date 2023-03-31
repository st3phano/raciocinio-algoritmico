'''
Faça um programa que peça o nome de um mês e informe quantos dias ele tem
Considere fevereiro sempre com 28 dias
'''

nomeMes = input("Digite o nome de um mês: ").lower()

diasPorMes = {"janeiro": 31, "fevereiro": 28, "março": 31, "abril": 30, "maio": 31, "junho": 30, "julho": 31,
					"agosto": 31, "setembro": 30, "outubro": 31, "novembro": 30, "dezembro": 31}

if (nomeMes in diasPorMes):
	print(f"O mês de {nomeMes} tem {diasPorMes[nomeMes]} dias")
else:
	print("Mês inválido")
