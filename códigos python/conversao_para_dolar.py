"""Descrição
Escreva um programa que realize a conversão de dólar para real: para cada valor lido em dólar da entrada padrão, será exibido o correspondente em reais (1 dólar = 3.55 reais).

Formato de entrada

Um número real (float)  que representa um valor em dólares.

Formato de saída

Um número real com duas casas decimais (float) que representa o valor de entrada convertido para reais"""


dolar = float(input())
reais = 3.55
conversao = dolar*reais
print ("{:.2f}".format(conversao))