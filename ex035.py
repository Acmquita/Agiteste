from math import ceil
def cabecalho():
	print('*' * 35)
	print(' '*5,'SIMULADOR DE EMPRÉSTIMO', ' '*5)
	print('*' * 35)


def valoremprestimo():
	emprestimo = float(input(f'Qual o valor que vai ser emprestado? Máximo é {valor}'))
	while emprestimo > valor:
		emprestimo = float(input('Valor maior que a margem do cliente. Tente um valor mais baixo.'))
	return emprestimo

def confirm():
	confirmation = str(input(f'O valor que deseja emprestar é R${emprestimo}? [S] para Sim, [N] para Não:')).lower().strip()[0]
	while confirmation not in 'sn':
		confirmation = str(input('Opção Inválida! [S] para Sim, [N] para Não: '))

def calculo():
	salario = float(input('Qual a renda do comprador? '))
	global percent 
	percent = salario*(30/100)
	print('A parcela máxima que pode ser paga pelo comprador é R${}'.format(percent))

	valor = 72 * percent
	qtd_prestacao = ceil(valor / percent) # calculo da quantidade prestação , considerando o valor máximo da prestação
	print(f'Com essa renda de {salario} o comprador poderá tomar no máximo {valor} emprestado. Com o prazo máximo de {qtd_prestacao} meses')
	return valor

def confirmPrazo():
	for parc in range(24, 72, 6):
			print(f'{parc}x{emprestimo/parc:.2f}')

if __name__ == '__main__':
	cabecalho()
	valor = calculo()
	emprestimo = valoremprestimo()
	confirm()
	confirmPrazo()

	