# Questao 2
# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

#Regras:
#1)Se o ano for divisível por 4, vá para a etapa 2. ...
#2)Se o ano for divisível por 100, vá para a etapa 3. ...
#3)Se o ano for divisível por 400, vá para a etapa 4. ...
#4)O ano é bissexto (ele tem 366 dias).
#5)O ano não é um ano bissexto (ele tem 365 dias).

ano = int(input('Digite o ano:'))

if (ano%4==0 and ano%100 != 0) or (ano%400==0):
    print ('Ano Bissexto')
else:
    print ('Ano nao eh bissexto')