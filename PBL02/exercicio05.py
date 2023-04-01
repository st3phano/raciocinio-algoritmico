'''
Faça um programa que peça o peso e a altura de uma pessoae calcule o seu IMC (índice de massa corporal)
e informe se ela está abaixo, dentro ou acima do peso
'''

pesoKg = float(print("Digite seu peso em quilogramas: "))
alturaMetros = float(print("Digite sua altura em metros: "))

imc = pesoKg / (alturaMetros ** 2)

if (imc < 18.5):
   print("Abaixo do peso ideal")
elif (imc < 25.0):
   print("No peso ideal")
else:
   print("Acima do peso")
