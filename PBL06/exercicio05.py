'''
Escreva um programa que crie uma lista de palavras e imprima a palavra mais
longa e a palavra mais curta da lista.
'''

from random import choice
from random import randint
from string import ascii_lowercase

QUANTIDADE_PALAVRAS_MIN = 3
QUANTIDADE_PALAVRAS_MAX = 10
quantidadePalavras = randint(QUANTIDADE_PALAVRAS_MIN, QUANTIDADE_PALAVRAS_MAX)

QUANTIDADE_LETRAS_MIN = 3
QUANTIDADE_LETRAS_MAX = 12
palavras = []
for _ in range(quantidadePalavras):
   palavras.append("".join(
                   [choice(ascii_lowercase)
                    for _ in range(randint(QUANTIDADE_LETRAS_MIN, QUANTIDADE_LETRAS_MAX))]))
print(palavras)

tamanhoPalavras = [[len(palavra), palavra] for palavra in palavras]
print(f"Maior palavra: {max(tamanhoPalavras)}")
print(f"Menor palavra: {min(tamanhoPalavras)}")
