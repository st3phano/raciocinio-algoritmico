'''
Implemente um programa em Python que solicita ao usuário 10 valores
inteiros. Verifique quantos são pares e quantos são ímpares. Imprima a
quantidade de valores pares e ímpares.
'''

pares = impares = 0

QUANTIDADE_INTEIROS = 10
print(f"Digite {QUANTIDADE_INTEIROS} valores inteiros, cada um em uma linha")
for _ in range(QUANTIDADE_INTEIROS):
   while not (inteiro := input(": ")).isdigit():
      print("Valor inválido, digite um valor inteiro!")
   
   if int(inteiro) % 2 == 0:
      pares += 1
   else:
      impares += 1

print(f"Você digitou {pares} valor(es) par e {impares} valor(es) ímpar")
