"""Descrição
Ler um número inteiro N e calcular todos os seus divisores.

Formato de entrada

A entrada contém um valor inteiro N (1 ≤ N ≤ 100000).

Formato de saída

Escreva todos os divisores positivos de N, um valor por linha."""



valor = int (input())

for i in range (1, valor+1):

    if (valor % i == 0):
        print (i)
    else: 
        pass