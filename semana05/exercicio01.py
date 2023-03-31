'''
Imprima na tela a tabuada de um número inteiro lido pelo teclado
'''

fatorA = int(input("Digite um número: "))

fatorB = 1
produto = fatorA
while (fatorB <= 10):
	print(f"{fatorA} x {fatorB} = {produto}")
	produto += fatorA
	fatorB += 1
