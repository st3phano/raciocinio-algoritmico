'''
Implemente um programa em Python para ler do teclado números
Caso o usuário forneça um número igual a -1, o programa deve
fornecer a média dos números e encerrar
'''

somaNumeros = 0
quantidadeNumeros = 0
lerNumero = lambda: float(input("Digite um número (-1 para encerrar): "))
while ((numeroAtual := lerNumero()) != -1):
   somaNumeros += numeroAtual
   quantidadeNumeros += 1

if (quantidadeNumeros > 0):
   mediaNumeros = somaNumeros / quantidadeNumeros
else:
   mediaNumeros = 0
print(f"A média dos números fornecidos é: {mediaNumeros}")
