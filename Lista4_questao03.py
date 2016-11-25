# Questao 3
# 3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 
# Imprima os três vetores.


import random

vet1 = []
vet2 = []
vet3 = []

for x in range(10):
	n = random.randint(1,100)
	m = random.randint(1,100)
	vet1.append(n)
	vet2.append(m)
	vet3.append(n)	
	vet3.append(m)
	
print "Vetor 1 = ", vet1
print "Vetor 2 = ", vet2
print "Vetor 3 = ", vet3
