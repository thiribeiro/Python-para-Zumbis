# Questao 3
# 3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento


habA = 80000
taxaA = 0.03
habB = 200000
taxaB = 0.015
anos = 0

while habB >= habA:
	habA = habA + habA*taxaA
	habB = habB + habB*taxaB
	anos += 1

print('Populacao pais A:%.2f ' %habA)
print('Populacao pais B:%.2f ' %habB)	
print('Foram necessarios %d anos para a Populacao do Pais A passar ou igualar a populacao do pais B' %anos)
