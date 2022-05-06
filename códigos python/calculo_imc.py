"""Descrição
Faça um programa que receba as características (massa e altura) de uma pessoa e retorne seu IMC - Índice de Massa Corporal.

O valor de saída deve ser arredondado usando 2 casas decimais.

Formato de entrada

A massa em Kg que pode estar entre 1 e 500.

A altura em metros (m) que pode estar entre 1 e 2.8

Formato de saída

O índice de massa corporal da pessoa.

O valor de saída deve ser arredondado usando 2 casas decimais.
"""

massa = float(input())
altura = float(input())
imc = massa/(altura**2)
print ("{:.2f}".format(imc))