'''
Faça um programa que peça um número inteiro e verifique se ele é primo ou não
'''

numeroInt = int(input("Digite um número inteiro: "))

if ((numeroInt < 2) or (numeroInt % 2 == 0)):
   ehPrimo = False
else:
   ehPrimo = True
   divisor = 3
   divisorMaximo = (numeroInt ** 0.5)
   while (divisor <= divisorMaximo):
      if (numeroInt % divisor == 0):
         primo = False
         break
      divisor += 2

if (ehPrimo):
   print("O número é primo")
else:
   print("O número nâo é primo")
