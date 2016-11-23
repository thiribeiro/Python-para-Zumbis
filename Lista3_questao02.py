# Questao 2
# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

user = input('digite o nome: ')
senha = input('digite a senha: ')

while user == senha:
	print('Erro! nome nao pode ser igual a senha!')
	nome = input('digite o nome: ')
	senha = input('digite a senha: ')