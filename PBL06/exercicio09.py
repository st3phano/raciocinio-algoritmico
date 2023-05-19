'''
Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe
suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de
uma determinada letra e informe se ele acertou ou errou
'''

from random import randrange
from string import ascii_uppercase

def meuShuffle(lista: list) -> list:
   for i in range(len(lista)):
      aux = lista[i]
      j = randrange(len(lista))
      lista[i] = lista[j]
      lista[j] = aux

   return lista

letrasAlfabetoEmbaralhadas = meuShuffle(list(ascii_uppercase))
print(letrasAlfabetoEmbaralhadas)

indiceLetraSorteada = randrange(len(letrasAlfabetoEmbaralhadas))
while (not (palpitePosicao := input("Tente adivinhar a posição da letra "
                                   f"{letrasAlfabetoEmbaralhadas[indiceLetraSorteada]}: "))
                                   .isdecimal()):
    print("Posição inválida!")

palpitePosicao = int(palpitePosicao)
if (palpitePosicao - 1 == indiceLetraSorteada):
   print("Você acertou!")
else:
   print("Você errou!")
