# Questao 7
#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

tempCel = float(input('Digite a temperatura(em celsius): '))
tempFar = (9*tempCel)/5 + 32
print('O resultado da temperatura em Fahrenheit é: %.2f' %tempFar)
