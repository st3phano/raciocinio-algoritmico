'''
Escreva um programa que receba 10 números do teclado
e exiba a quantidade de números pares e ímpares lidos
'''

quantidadeNumerosPares = 0
quantidadeNumerosImpares = 0
for i in range(10):
	numeroIntAtual = int(input(f"Digite o {i + 1} número inteiro: "))
	if (numeroIntAtual % 2 == 0):
		quantidadeNumerosPares += 1
	else:
		quantidadeNumerosImpares += 1

print(f"Foram digitados {quantidadeNumerosPares} números pares "
		f"e {quantidadeNumerosImpares} números ímpares")
