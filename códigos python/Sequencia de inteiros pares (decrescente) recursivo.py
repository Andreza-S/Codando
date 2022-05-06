"""Descrição
Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.

Formato de entrada

Um inteiro positivo N.

Formato de saída

Uma sequência de pares de 0 a N linha à linha."""


def Sequencia_pares_crescente (n):

    if n >= 0:
        if n % 2 == 0:
            print (n)
    else:
        return 0
    
    Sequencia_pares_crescente(n-1)



numero = int (input())
Sequencia_pares_crescente(numero)