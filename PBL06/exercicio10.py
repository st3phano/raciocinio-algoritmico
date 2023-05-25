'''
Tente agora fazer o jogo da forca, mas utilizando listas ao invés de vetores.
'''

import random
import re

palavras = ["abacaxi", "bicicleta", "chocolate", "dinossauro", "elefante", "futebol", "girassol", "cadeira", "igreja", "janela"]
palavraSorteada = random.choice(palavras)

CARACTERE_OCULTACAO = '_'
palavraEscondida = [CARACTERE_OCULTACAO] * len(palavraSorteada)

tentativasRestantes = 2 * len(palavraSorteada)
while ((CARACTERE_OCULTACAO in palavraEscondida) and (tentativasRestantes > 0)):
   print(f"\nTENTATIVAS RESTANTES: {tentativasRestantes}")
   tentativasRestantes -= 1

   print(f"Palavra: {''.join(palavraEscondida)}")

   # recebe e valida uma letra digitada
   letraPalpite = input("Digite um letra: ")
   REGEX_LETRA = r"[a-zA-Z]"
   while (re.fullmatch(REGEX_LETRA, letraPalpite) == None):
      letraPalpite = input("Entrada inválida! Por favor digite UMA LETRA: ")
   letraPalpite = letraPalpite.lower()

   if (letraPalpite in palavraEscondida):
      print(f"A letra '{letraPalpite}' já foi encontrada na palavra!")
   elif (letraPalpite not in palavraSorteada):
      print(f"A letra '{letraPalpite}' não pertence a palavra!")
   else:
      i = -1
      for _ in range(palavraSorteada.count(letraPalpite)):
         i = palavraSorteada.index(letraPalpite, i + 1)
         palavraEscondida[i] = letraPalpite

if (CARACTERE_OCULTACAO not in palavraEscondida):
   print(f"Parabéns! Você acertou a palavra '{palavraSorteada}'.")
else:
   print("Infelizmente suas tentativas acabaram.")
