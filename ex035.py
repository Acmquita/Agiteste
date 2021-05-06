from math import ceil
def cabecalho():
	print('*' * 35)
	print(' '*5,'SIMULADOR DE EMPRÉSTIMO', ' '*5)
	print('*' * 35)

cabecalho()

salario = float(input('Qual a renda do comprador? '))
percent = salario*(30/100)
print('A parcela máxima que pode ser paga pelo comprador é R${}'.format(percent))

valor = 72 * percent
qtd_prestacao = ceil(valor / percent) # calculo da quantidade prestação , considerando o valor máximo da prestação
print(f'Com essa renda de {salario} o comprador poderá tomar no máximo {valor} emprestado. Com o prazo máximo de {qtd_prestacao} meses')

emprestimo = float(input(f'Qual o valor que vai ser emprestado? Máximo é {valor}'))
while emprestimo > valor:
	emprestimo = float(input('Valor maior que a margem do cliente. Tente um valor mais baixo.'))

confirmation = str(input(f'O valor que deseja emprestar é R${emprestimo}? [S] para Sim, [N] para Não:')).lower()
while confirmation not in 'sn':
	confirmation = str(input('Opção Inválida! [S] para Sim, [N] para Não: '))
