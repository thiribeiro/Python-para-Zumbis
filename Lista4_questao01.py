# Questao 1
# 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random

lista1 = []
maior = 0
menor = 100

for i in range(10):
	n = random.randint(1,100)
	lista1.append(n)

	if n < menor: 
		menor = n
	if n > maior:
		maior = n

lista1.sort()

print lista1
print("\nMenor: %d - Maior: %d" %(menor, maior))
