"""Descrição
Faça um programa que imprima todos os números ímpares entre dois números dados.

Formato de entrada

Dois números inteiros, n e m, separados por um final de linha.

Formato de saída

Todos os números ímpares maiores ou iguais a n e menores ou iguais a m, separados por um final de linha."""


nInicial = int (input())
nFinal = int (input())


for i in range (nInicial, nFinal+1):
    if (i % 2 != 0):
        print (i)
    
    else:
        pass