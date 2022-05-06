"""Descrição
Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente. 

Formato de entrada

Um inteiro positivo N.

Formato de saída

Uma sequência de números de 0 à N linha à linha."""


def Sequencia_pares_crescente (n):

    if n < 0:
        return 
    
    Sequencia_pares_crescente(n-1)

    if n % 2 == 0:
        print (n)

numero = int (input())
Sequencia_pares_crescente(numero)