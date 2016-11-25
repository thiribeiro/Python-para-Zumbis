# Questao 5
# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

precoMer = float(input('Digite o valor da mercadoria: '))
desc = float(input('Digite o percentual do desconto: '))
percent = desc / 100
descVal = precoMer * percent
precoPag = precoMer - descVal
print('O valor do Desconto é: %.2f' %descVal)
print('O valor do preço a pagar é: %.2f' %precoPag)