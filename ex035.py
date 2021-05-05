from math import ceil
print('*' * 35)
print(' '*5,'SIMULADOR DE EMPRÉSTIMO', ' '*5)
print('*' * 35)
salario = float(input('Qual a renda do comprador? ')) 
percent = salario*(30/100)
print('A parcela máxima que pode ser paga pelo comprador é R${}'.format(percent))


valor = float(input('Qual o valor do imóvel? '))
prestação = ceil(valor / percent)
print(prestação)
parcela = valor/prestação
if prestação > 30:
	valor = valor + valor*5/1000
#for i in range(prestação, 80):
	#parcela = valor/i
while parcela > valor/80:
	parcela = valor/prestação
	print('{} parcelas de {:.2f}'. format(prestação, parcela))
	#parcela = parcela + (parcela*5/1000)
	prestação=prestação+1







#parcela = valor/prazo

#if parcela > percent:
#	print('O empréstimo foi negado, pois a parcela é de R$ {} e a margem do comprador é de R$ {:.2f}. '.format(parcela, percent))
#elif percent >= parcela:
#	print('O empréstimo foi aprovado! A parcela ficará de R$ {:.2f}, durante {} meses'.format(parcela, prazo))	