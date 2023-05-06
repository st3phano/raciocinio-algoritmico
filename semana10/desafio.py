'''
Implemente um programa em Python para verificar quantos números
uma aposta acertou na Mega Sena. O programa deve ler do teclado
os 6 números apostados e comparar com os 6 números sorteados.
Ao final, o programa deve exibir os números sorteados, números
jogados e quantidade de acertos.
'''

from random import randint
import re

NUMERO_MIN_MEGA_SENA = 1
NUMERO_MAX_MEGA_SENA = 60
QUANTIDADE_NUMEROS_MEGA_SENA = 6

numerosSorteados = [0] * QUANTIDADE_NUMEROS_MEGA_SENA
# sorteia os números da Mega Sena
for i in range(QUANTIDADE_NUMEROS_MEGA_SENA):
   numerosSorteados[i] = randint(NUMERO_MIN_MEGA_SENA, NUMERO_MAX_MEGA_SENA)

numerosApostados = [0] * QUANTIDADE_NUMEROS_MEGA_SENA
# requisita os números da aposta
for i in range(QUANTIDADE_NUMEROS_MEGA_SENA):
   numero = input(f"Digite o {i + 1}º número de sua aposta: ")

   # previne entradas que não sejam números inteiros diferentes dos já digitados
   inteiroRegex = r"[-+]?\d+"
   while ((re.fullmatch(inteiroRegex, numero) == None) or
          (int(numero) < NUMERO_MIN_MEGA_SENA) or
          (int(numero) > NUMERO_MAX_MEGA_SENA) or
          (int(numero) in numerosApostados)):
      numero = input(f"Digite um número entre {NUMERO_MIN_MEGA_SENA} e {NUMERO_MAX_MEGA_SENA}"
                     " que ainda não foi digitado: ")
      
   numerosApostados[i] = int(numero)

# conta a quantidade de acertos da aposta
acertosAposta = 0
for i in range(QUANTIDADE_NUMEROS_MEGA_SENA):
   if (numerosApostados[i] in numerosSorteados):
      acertosAposta += 1

print(f"Números sorteados:\t{numerosSorteados}")
print(f"Números apostados:\t{numerosApostados}")
print(f"Quantidade de acertos:\t{acertosAposta}")
