'''
Implemente um programa em Python que solicita ao usuário 10 valores
inteiros. Verifique quantos são pares e quantos são ímpares. Imprima a
quantidade de valores pares e ímpares.
'''

pares = impares = 0

QUANTIDADE_INTEIROS = 10
print(f"Digite {QUANTIDADE_INTEIROS} valores inteiros")
for i in range(1, QUANTIDADE_INTEIROS + 1):
   inteiro = input(f"{i}º: ")
   while not inteiro.isdecimal():
      inteiro = input("Entrada inválida, digite um valor inteiro: ")
   
   if int(inteiro) % 2 == 0:
      pares += 1
   else:
      impares += 1

print(f"Você digitou {pares} valor(es) par e {impares} valor(es) ímpar")
