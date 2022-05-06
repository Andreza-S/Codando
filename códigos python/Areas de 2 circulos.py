"""Descrição
Escreva um programa que leia os valores (reais) dos raios de dois círculos diferentes e informe qual dos dois possui área maior ou se possuem a mesma área.

Use pi = 3.14

Formato de entrada

Os raios (tipo float) de 2 círculos em sequência.

Formato de saída

Caso a área do primeiro círculo seja maior, escreva na saída: "Primeiro círculo"

Caso a área do segundo círculo seja maior, escreva na saída: "Segundo círculo"

Caso sejam iguais, escreva: "Iguais"""


RC1 = float (input ())
RC2 = float (input ())
areac1 = (RC1**2)*3.14
areac2 = (RC2**2)*3.14
if areac1 > areac2:
    print ("Primeiro circulo")
elif areac1 < areac2:
    print ("Segundo circulo")
else:
    print ("Iguais")