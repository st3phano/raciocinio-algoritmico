'''
Faça um programa que peça um número inteiro e verifique se ele é primo ou não
'''

numeroInt = int(input("Digite um número inteiro: "))

primo = True
divisor = 2
divisorMaximo = numeroInt ** 0.5
while (primo and (divisor <= divisorMaximo)):
	if (numeroInt % divisor == 0):
		primo = False
	divisor += 1

if (primo):
	print("O número é primo")
else:
	print("O número nâo é primo")
