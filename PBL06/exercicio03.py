'''
Escreva um programa que peça ao usuário uma frase e converta cada palavra
em uma lista separada. Imprima a lista na tela.
'''

frase = input("Digite uma frase: ")
palavras = [list(palavra) for palavra in frase.split()]

print(palavras)
