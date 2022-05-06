"""Descrição
Leia 10 números inteiros.

Depois leia mais um número inteiro x.

Sua missão é imprimir quantas vezes x apareceu entre os 10 primeiros inteiros lidos.

Formato de entrada

11 linhas, cada uma contendo um inteiro.

A última linha é o número x a ser buscado.

Os inteiros são todos entre 0 e 10000.

Formato de saída

Um número inteiro indicando quantas vezes x apareceu."""


QTD_DE_N = 10
lista_de_n = []


for i in range (QTD_DE_N+1):
    if (i < QTD_DE_N):
        n = int (input())
        lista_de_n.append(n)
    
    if (i == QTD_DE_N):
        x = int (input())
        qtd_de_x = lista_de_n.count(x)

        print (qtd_de_x)