"""Descrição
Crie um programa que receba como entrada dois números naturais, A e B (A <= B), e exiba todos os números inteiros do intervalo fechado crescente [ A .. B ], ou seja, A e B também deverão ser exibidos. 

Formato de entrada

Na primeira linha o número natural correspondente ao A; na segunda linha o número natural correspondente ao B.

Formato de saída

Todos os números naturais entre A e B, inclusive A e B, um por linha."""


nInicial = int (input())
nFinal = int (input())

for i in range (nInicial,nFinal+1):
    print (i)