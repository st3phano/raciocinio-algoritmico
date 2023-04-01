'''
Faça um programa que peça três números inteiros e determine qual é o maior e qual é o menor
'''

def maiorValor(valorA, valorB):
   return (valorA + valorB + abs(valorA - valorB)) / 2

def menorValor(valorA, valorB):
   return (valorA + valorB - abs(valorA - valorB)) / 2

###########################################################################################

numerosInt = []
QUANTIDADE_NUMEROS_INT = 3
for i in range(QUANTIDADE_NUMEROS_INT):
   numerosInt.append(int(input(f"Digite o {i + 1} número inteiro: ")))

maiorNumero = maiorValor(maiorValor(numerosInt[0], numerosInt[1]), numerosInt[2])
print(f"O maior número entre {numerosInt} é {int(maiorNumero)}")

menorNumero = menorValor(menorValor(numerosInt[0], numerosInt[1]), numerosInt[2])
print(f"O menor número entre {numerosInt} é {int(menorNumero)}")
