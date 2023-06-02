'''
Escreva uma função chamada "inverter" que receba uma string como parâmetro e
imprime a string invertida.
'''

def inverter(texto: str) -> None:
   for i in range(len(texto) - 1, -1, -1):
      print(texto[i], end='')
   print()

inverter("essa string será impressa invertida")
