import random
import re

palavras = ["abacaxi", "bicicleta", "chocolate", "dinossauro", "elefante", "futebol", "girassol", "cadeira", "igreja", "janela"]

palavraSorteada = random.choice(palavras)
CARACTERE_OCULTACAO = '_'
palavraEscondida = [CARACTERE_OCULTACAO] * len(palavraSorteada)

letrasParaDescobrir = len(palavraSorteada)
numeroTentativas = 2 * len(palavraSorteada)
while (letrasParaDescobrir > 0 and numeroTentativas > 0):
   print(f"\nTENTATIVAS RESTANTES: {numeroTentativas}")
   numeroTentativas -= 1

   print(f"Palavra:", end=' ')
   for ch in palavraEscondida:
      print(ch, end="")
   print()

   # recebe e valida uma letra digitada
   letraPalpite = input("Digite um letra: ")
   REGEX_LETRA = r"[a-zA-Z]"
   while (re.fullmatch(REGEX_LETRA, letraPalpite) == None):
      letraPalpite = input("Entrada inválida! Por favor digite UMA LETRA: ")
   letraPalpite = letraPalpite.lower()

   # a letra digitada já havia sido encontrada?
   letraJaFoi = False
   i = 0
   while (not letraJaFoi and i < len(palavraEscondida)):
      if (palavraEscondida[i] == letraPalpite):
         print(f"A letra '{letraPalpite}' já foi encontrada na palavra!")
         letraJaFoi = True
      i += 1

   if (not letraJaFoi):
      # a letra digitada pertence a palavra escondida?
      letraEncontrada = False
      for i in range(len(palavraSorteada)):
         if (palavraSorteada[i] == letraPalpite):
            letraEncontrada = True
            letrasParaDescobrir -= 1
            palavraEscondida[i] = letraPalpite
      if (not letraEncontrada):
         print(f"A letra '{letraPalpite}' não pertence a palavra!")

if (letrasParaDescobrir == 0):
   print(f"Parabéns! Você acertou a palavra '{palavraSorteada}'.")
else:
   print("Infelizmente suas tentativas acabaram.")
