# Questao 4
# 4. Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o valor 1: '))
n2 = float(input('Digite o valor 2: '))
n3 = float(input('Digite o valor 3: '))

if n1>n2 and n1>n3:
	maior = n1
elif n2>n1 and n2>n3:
	maior = n2
else:
	maior = n3

print('O maior numero eh: %.2f' %maior)