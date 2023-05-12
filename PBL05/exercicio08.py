'''
Faça um algoritmo que leia um número positivo e imprima seus divisores.
'''

inteiroPositivo = input("Digite um número inteiro positivo: ")
while (not inteiroPositivo.isdecimal()):
   inteiroPositivo = input("Número inválido! Digite um inteiro positivo: ")

inteiroPositivo = int(inteiroPositivo)
print("Divisores:", end=' ')
for divisor in range(2, (inteiroPositivo // 2) + 1):
   if (inteiroPositivo % divisor == 0):
      print(f"[{divisor}]", end=' ')
print()
