'''
Faça um programa que peça o salário de um funcionário e calcule o valor do seu aumento
Para salários acima de R$ 1.500,00, o aumento é de 10%
Para salários iguais ou inferiores a R$ 1.500,00, o aumento é de 15%
'''

salarioFuncionario = float(input("Digite o seu salário: "))

if (salarioFuncionario > 1500.0):
	porcentagemAumento = 0.10
else:
	porcentagemAumento = 0.15

valorAumento = salarioFuncionario * porcentagemAumento
print(f"O valor do seu aumento é de R${valorAumento:.2f}")
