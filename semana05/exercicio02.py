'''
Implemente um programa em Python para ler do teclado a nota de um aluno
Verifique se o valor lido é uma nota válida (maior que 7)
Se não for, ler este valor até que a mesma seja válida
'''

lerNotaAluno = lambda: float(input("Digite a nota do aluno: "))
while ((notaAluno := lerNotaAluno()) <= 7):
   print("Nota inválida")

print(f"A nota do aluno é {notaAluno:.2f}")
