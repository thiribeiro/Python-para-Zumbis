# Questao 7
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
# Obs. : somente são vendidos um número inteiro de latas.

#lata = 18 litros , R$ 80.00 -----> 1 litro de tinta cobre 3m. 1 lata(18 litros) cobre 54m
area = float(input('Digite o valor da area(em Metros): '))

if area <= 54:
	qtdLatas = 1
	precoTotal = 80
else:
	qtdLatas = area/54
	qtdLatas = round(qtdLatas)
	precoTotal = qtdLatas*80
	
print('Qtd de Latas a serem Compradas: %d' %qtdLatas)
print('Preco Total: R$ %.2f' %precoTotal)