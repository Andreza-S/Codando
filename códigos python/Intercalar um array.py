"""Descrição
Você deve intercalar dois arrays de números inteiros.

Formato de entrada

Na primeira linha você receberá um número inteiro n indicando o tamanho de cada um dos arrays.

As próximas n linhas correspondem aos elementos do primeiro array.

Depois seguirão mais n linhas correspondendo aos elementos do segundo array.

Formato de saída

Você deve imprimir 2n linhas com os arrays intercalados. Por exemplo, se a entrada for:

3

1

5

9

2

4

8

 

Você deve imprimir:

1

2

5

4

9

8"""



n_numeros = int (input())

lista_1 = []
lista_2 = []



for i in range (n_numeros):
    numero = int (input())
    lista_1.append(numero)

for j in range (n_numeros):

    numero = int (input())
    lista_2.append(numero)


for g in range (n_numeros):
        print (lista_1[g])
        print (lista_2[g])