'''
Objetivo: Implementar uma calculadora em Python que possa realizar as quatro
operações básicas (adição, subtração, multiplicação e divisão) através de um menu de
opções. O usuário deve informar a operação desejada, e a calculadora realizará
operações com apenas 2 valores. O programa deve permitir que o usuário execute
quantas operações quiser, sem que a execução seja interrompida. A opção 0 deverá ser
selecionada para encerrar o programa.
'''

def selecionarOperador():
	operadores = {"somar": '+',
					  "subtrair": '-',
					  "multiplicar": '*',
					  "dividir": '/',
					  "sair": '0'}

	# Imprime um menu com todas as operações disponíveis
	print("----| Menu Calculadora |----")
	for nome, operador in operadores.items():
			print(f"{operador} : {nome}")

	# Impede que o usuário digite uma operação inexistente
	operador = input("Digite a operação desejada: ")
	while (operador not in operadores.values()):
		operador = input("Operação inválida!\nTente novamente: ")

	return operador

def realizarOperacao(valores, operador):
	resultado = valores[0]

	funcoesOperadoras = {'+': lambda x, y: x + y,
								'-': lambda x, y: x - y,
								'*': lambda x, y: x * y,
								'/': lambda x, y: (x / y) if (y != 0) else
														float("-inf") if (x < 0) else
														float("inf")}
	funcaoOperadora = funcoesOperadoras[operador]
	# Faz 'resultado [operador] valor' para todos os valores restantes na lista
	for valor in valores[1:]:
		resultado = funcaoOperadora(resultado, valor)

	return resultado

def mostrarResultado(valores, operacao, resultado):
	for valor in valores[:-1]:
		print(f"{valor} {operacao}", end = ' ')
	print(f"{valores[-1]} = {resultado:.2f}")

###########################################################################################

valores = []
while ((operador := selecionarOperador()) != '0'):
	quantidadeValores = int(input("Quantos valores serão utilizados na operação? "))
	# Impede que o usuário digite uma quantidade de valores < 1
	while (quantidadeValores < 1):
		quantidadeValores = int(input("Digite uma quantidade positiva!\nTente novamente: "))

	# Lê os valores um por um
	for i in range(quantidadeValores):
		valores.append(float(input(f"Digite o {i + 1} valor: ")))

	resultado = realizarOperacao(valores, operador)
	mostrarResultado(valores, operador, resultado)

	valores.clear()
	print('\n')

print("Encerrando a calculadora...")
