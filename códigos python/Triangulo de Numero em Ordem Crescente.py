"""Descrição
Faça um programa que dado um número inteiro n, imprima n linhas, onde cada linha deve seguir o seguinte padrão:

1

22

333

4444

55555

666666

7777777

…

nnnnnnnnnn

Formato de entrada

Um número inteiro positivo n. ( 1<= n <= 30 )

Formato de saída

n linhas contendo inteiros de acordo com o padrão especificado na descrição"""


n = int (input())

nrepetir = 0

for i in range(1, n+1):
    nrepetir = i
    if i >= 2:
        print ("")
    for nrep in range (i):
        print ("{}".format (nrepetir), end = "")