"""Descrição
Escreva uma função recursiva chamada ContaDigitosPares que receba como entrada um número e retorne a quantidade de dígitos pares que o compõem.

Ex: 234 tem 3 dígitos, mas apenas 2 são pares

Formato de entrada

Um número inteiro

Formato de saída

Um número inteiro"""


def ContaDigitosPares (n):

    qtd_digitos_pares = 0

    for i in range (len(n)):
        inteiro_n = int (n[i]) 
        if (inteiro_n % 2 == 0):
            qtd_digitos_pares += 1
        
    return (print (qtd_digitos_pares))

numero = (input())

(ContaDigitosPares(numero))