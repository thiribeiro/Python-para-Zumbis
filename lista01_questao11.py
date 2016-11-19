# Questao 11
# 11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

numero = 2**1000000    			# 2 elevado a um milhão
numdigit = str(numero)			# Transformando numero em string
len(numdigit)					# Pegando o tamanho do resultado da string