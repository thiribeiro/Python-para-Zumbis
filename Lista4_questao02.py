# Questao 2
# 2. Sorteie 20 inteiros entre 1 e 100 numa lista. 
# Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random

listaInteira = []
listaPar = []
listaImpar = []

for i in range(20):
	n = random.randint(1,100)
	listaInteira.append(n)
	if n % 2 == 0:
		listaPar.append(n)
	else:
		listaImpar.append(n)
		
	
print "Lista Inteira = ", listaInteira
print "Lista Par = ",  listaPar
print "Lista Impar = ",  listaImpar

