# Questao 1
# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = float(input('Digite o lado 1:'))
lado2 = float(input('Digite o lado 2:'))
lado3 = float(input('Digite o lado 3:'))

# Regra para validar um triangulo: 
# Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e 
# menor que a soma dos outros dois lados. Veja o resumo da regra abaixo: 
# | b - c | < a < b + c 
# | a - c | < b < a + c 
# | a - b | < c < a + b 

regra1 = abs(lado2 - lado3) < lado1 < (lado2 + lado3)
regra2 = abs(lado1 - lado3) < lado2 < (lado1 + lado3)
regra3 = abs(lado1 - lado2) < lado3 < (lado1 + lado2)

if regra1 and regra2 and regra3 == True:
	print('Ha possibilidade de existir um triangulo com os valores dados!')
	if lado1 == lado2 and lado2 == lado3:
		print('Triangulo Equilatero!')
	elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
		print('Triangulo Isoceles!')
	else:
		print('Triangulo Escaleno!')
else:
	print('Nao ha possibilidade de existir um triangulo com os valores dados!')
	
