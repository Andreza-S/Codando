"""Descrição
Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é o maior. Se os números forem iguais, imprima qualquer um deles.

Formato de entrada

Dois valores inteiros.

Formato de saída

O maior dentre os 2 valores fornecidos."""


N1 = int (input())
N2 = int (input())
if (N1 > N2):
    print (N1)
elif ( N1 < N2):
    print (N2)
elif ( N1 == N2):
    print (N1)