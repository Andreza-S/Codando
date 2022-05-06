"""Descrição
Calcule os fatoriais de uma sequência de números dada.

Formato de entrada

O programa receberá uma sequência de inteiros n, onde 0<=n<=12.
O programa encerra a sua execução quando o número n dado for -1.

Formato de saída

Para cada n, deve-se imprimir um inteiro k seguido de um final de linha, correspondendo ao fatorial."""

while True:
    fatorial = 1
    n = int (input())

    if (n == -1):
        exit()

    for i in range (1,n):
        fatorial += (i * fatorial)

    print (fatorial)