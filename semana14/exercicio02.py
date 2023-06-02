'''
Escreva uma função chamada "maior" que receba três números como parâmetros e
retorne o maior entre eles.
'''

def maior(a: float, b: float, c: float) -> float:
   maior = a

   if (b > maior):
      maior = b

   if (c > maior):
      maior = c

   return maior

print(maior(-1, 12, 128))
