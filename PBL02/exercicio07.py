'''
Faça um programa que peça as notas de três provas de um aluno e calcule a média
Informe se o aluno está aprovado (média maior ou igual a 7),
em recuperação (média entre 5 e 7) ou reprovado (média abaixo de 5)
'''

notasProvas = []
QUANTIDADE_PROVAS = 3
somatorioNotasProvas = 0
for i in range(QUANTIDADE_PROVAS):
	notasProvas.append(float(input(f"Digite a nota da prova {i + 1}: ")))
	somatorioNotasProvas += notasProvas[i]

mediaNotasProvas = somatorioNotasProvas / QUANTIDADE_PROVAS
MEDIA_MINIMA_APROVACAO = 7.0
MEDIA_MINIMA_RECUPERACAO = 5.0
if (mediaNotasProvas < MEDIA_MINIMA_RECUPERACAO):
	print("Reprovado")
elif (mediaNotasProvas < MEDIA_MINIMA_APROVACAO):
	print("Recuperação")
else:
	print("Aprovado")
