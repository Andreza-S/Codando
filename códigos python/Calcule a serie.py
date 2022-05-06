"""Descrição
Escreva um programa que calcule os N termos da série S  abaixo:

 S = (1/3) + (2/6) + (3/9) + (4/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.

Formato de entrada

Um valor N que representa a quantidade de termos da série.

Formato de saída

Os termos da série e o valor da soma com precisão de 2 casas decimais."""


n = int (input())
s = 0

dividendo = 0
divisor = 0

for i in range (n):
    dividendo += 1
    divisor += 3
    if i == n -1:
        print( "{}/{}".format (dividendo, divisor), end ="")
    else:
        print ("{}/{} +".format(dividendo, divisor), end = " ")
    s += dividendo/divisor

print("\n{:.2f}".format (s))