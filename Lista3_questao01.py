# Questao 1
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = input("digite um numero de 0 a 10 ---> ")
while 0 > numero or 10 < numero:
    numero = input("digite um numero de 0 a 10 ---> ")