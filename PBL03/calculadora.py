'''
	Objetivo: Implementar uma calculadora em Python que possa realizar as quatro
	operações básicas (adição, subtração, multiplicação e divisão) através de um menu de
	opções. O usuário deve informar a operação desejada, e a calculadora realizará
	operações com apenas 2 valores. O programa deve permitir que o usuário execute
	quantas operações quiser, sem que a execução seja interrompida. A opção 0 deverá ser
	selecionada para encerrar o programa.
'''

def selecionarOperacao():
	print(
"""
----| Menu Calculadora |----
+ Somar
- Subtrair
* Multiplicar
/ Dividir
0 Sair
"""
	)

	return input("Digite sua opção: ")

def mostrarResultado(valores, quantidadeValores, operacao, resultado):
	for i in range(quantidadeValores - 1):
		print(f"{valores[i]} {operacao} ", end = "")
	print(f"{valores[-1]} = {resultado:.2f}")

###########################################################################################

valores = []
while ((operacao := selecionarOperacao()) != '0'):
	# Lê quantos e quais valores o usuário deseja
	quantidadeValores = int(input(f"Quantos valores deseja '{operacao}'? "))
	for i in range(quantidadeValores):
		valores.append(float(input(f"Digite o {i + 1} valor: ")))

	# Realiza a operação escolhida
	resultadoValido = True
	resultado = valores[0]
	if (operacao == '+'):
		for i in range(1, quantidadeValores):
			resultado += valores[i]
	elif (operacao == '-'):
		for i in range(1, quantidadeValores):
			resultado -= valores[i]
	elif (operacao == '*'):
		for i in range(1, quantidadeValores):
			resultado *= valores[i]
	elif (operacao == '/'):
		for i in range(1, quantidadeValores):
			if (valores[i] == 0):
				print("A divisão por 0 foi ignorada!")
			else:
				resultado /= valores[i]
	else:
		print("Operação inválida!")
		resultadoValido = False

	if (resultadoValido):
		mostrarResultado(valores, quantidadeValores, operacao, resultado)

	valores.clear()

print("Encerrando a calculadora...")
