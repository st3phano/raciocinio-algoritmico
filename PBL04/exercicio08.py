'''
Crie um programa com dois vetores de 10 posições e insira em outro
vetor, nas posições pares, os valores do primeiro e, nas posições
ímpares, os valores do segundo.
'''

TAMANHO_VETOR = 10
vetor1 = [0] * TAMANHO_VETOR
vetor2 = [0] * TAMANHO_VETOR
for i in range(TAMANHO_VETOR):
   vetor1[i] = i
   vetor2[i] = i * 10
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")

vetorAlternado = [0] * TAMANHO_VETOR
for i in range(TAMANHO_VETOR):
   vetorAlternado[i] = vetor1[i] if (i % 2 == 0) else vetor2[i]

print(vetorAlternado)
