# Questao 10
# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
#     Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias. 

qtdCigarrosDia = int(input('Digite a qtd de cigarros por dia: '))
qtdAnos = int(input('Digite a qtd de anos que vc fuma ou ja fumou: '))
totCigarros = (qtdAnos*365)*qtdCigarrosDia
diasPerdidos = (totCigarros*10)/24
print('A qtd de dias perdidos é: %d' %diasPerdidos)