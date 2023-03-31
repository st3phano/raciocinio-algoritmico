'''
Implemente um programa em Python para imprimir na tela o
somatório dos N primeiros números inteiros a partir do 1
Sendo N lido do teclado
'''

numeroIntLimite = int(input("Digite um número inteiro: "))

numeroIntAtual = 1
somatorioNumerosInt = 0
while (numeroIntAtual <= numeroIntLimite):
	somatorioNumerosInt += numeroIntAtual
	numeroIntAtual += 1

print(f"O somatório dos primeiros {numeroIntLimite} números inteiros é {somatorioNumerosInt}")
