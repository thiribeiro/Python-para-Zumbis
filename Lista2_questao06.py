# Questao 6
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato 
#e o salário líquido. 
#Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$


valHora = float(input('Digite o valor ganho por hora: '))
horasTrabMes = float(input('Digite a qtd de horas trabalhadas no mes: '))

salBruto = valHora * horasTrabMes
inss = salBruto * 0.08
ir = salBruto * 0.11
sind = salBruto * 0.05
descontos = inss + sind + ir
salLiquido = salBruto - descontos

print('Salario Bruto: %.2f, Pagou para o INSS: %.2f, Pagou para o sindicato: %.2f, Salario Liquido: %.2f' %(salBruto,inss,sind,salLiquido))