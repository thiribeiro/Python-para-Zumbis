# Questao 5
# 5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

while n1 % n2 != 0:
	n1, n2 = n2, n1 % n2 
	
print ('mdc = %d' %n2)