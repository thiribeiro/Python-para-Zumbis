# Questao 4
# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

valSal = float(input('Digite o valor do salário: '))
aumento = float(input('Digite o percentual do aumento: '))
percentual = aumento / 100
valAumento = valSal * percentual
novoSal = valSal + valAumento
print('O valor do Aumento é: %.2f' %valAumento)
print('O valor do novo salário é: %.2f' %novoSal)
