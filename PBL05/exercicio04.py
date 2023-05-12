'''
Leia várias idades e calcule a média entre as idades (usar uma variável para idade).
'''

QUANTIDADE_IDADES = 5
somaIdades = 0
for i in range(QUANTIDADE_IDADES):
   idade = input(f"Digite a {i + 1}a idade: ")
   while (not idade.isdecimal()):
      idade = input("Idade inválida! Tente novamente: ")
   somaIdades += int(idade)

mediaIdades = somaIdades // QUANTIDADE_IDADES
print(f"A média das idades é {mediaIdades} anos")
