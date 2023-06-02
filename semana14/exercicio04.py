'''
Escreva uma função chamada "media" que receba uma lista de números como
parâmetro e retorne a média desses números.
'''

def media(listaReais: list[float]) -> float:
   return sum(listaReais) / len(listaReais)

print(media([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]))
