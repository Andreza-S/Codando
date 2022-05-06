"""Descrição
Escreva um programa que leia números inteiros da entrada padrão até que seja informado um número negativo. A cada leitura o número lido deve ser escrito na saída padrão.

Formato de entrada

Números inteiros.

Formato de saída

Os números que foram lidos."""


while True:
    numero = int (input())
    if (numero < 0):
        print (numero)
        break
    else:
        print (numero)