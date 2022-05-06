"""Descrição
Escreva um programa que lê um inteiro N (1 <N <1000). Este N é o número de linhas de saída impressos por este programa.

Formato de entrada

O arquivo de entrada contém um número inteiro N.
Formato de saída

Imprima a saída de acordo com o exemplo dado."""


n = int (input())


for i in range (1,n+1):
    coluna_1 = (i**1)
    coluna_2 = (i**2)
    coluna_3 = (i**3)
    
    print ("{} {} {}".format (coluna_1, coluna_2, coluna_3))