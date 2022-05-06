"""Descrição
Escrever um programa que lê um número N. Este N é o tamanho de um array.

Em seguida, leia cada um dos N números do array, encontre o menor elemento desse array, a sua posição dentro do array e imprima essas informações.

Considere que o array começa na posição 0

Formato de entrada

A primeira linha da entrada contém um inteiro N (1 <N <1000), indicando o número de elementos que devem ser lidos no array de números inteiros. A segunda linha contém cada um dos valores de N, separadas por um espaço.

Obs: não haverão números repetidos.

Formato de saída

A primeira linha exibe a mensagem "Menor valor:" seguido por um espaço e o menor número lido na entrada. A segunda linha exibe a mensagem "POSIÇÃO:" seguido por um espaço e a posição do array em que o menor número é encontrado, lembrando que o array começa na posição zero."""


n = int (input())
lista__de_numeros = input().split()
lista_inteiros = list(map(int, lista__de_numeros))

menor_valor = 0
posicao = 0

for i in range (len(lista_inteiros)):
    if (i == 0):
        menor_valor = lista_inteiros[i]
        posicao = i
    else:
        if (lista_inteiros[i] < menor_valor):
            menor_valor = lista_inteiros[i]
            posicao = i

print ("Menor valor: {}".format (menor_valor))
print ("Posicao: {}".format (posicao))