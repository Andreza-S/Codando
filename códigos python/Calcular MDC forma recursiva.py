"""Descrição
Dois números naturais sempre têm divisores comuns. Por exemplo: os divisores comuns de 12 e 18 são 1,2,3 e 6. Dentre eles, 6 é o maior. Então chamamos o 6 de máximo divisor comum de 12 e 18 e indicamos m.d.c.(12,18) = 6.

Desenvolva uma função recursiva para calcular o m.d.c de dois inteiros.

Formato de entrada

Dois inteiros positivos.

Formato de saída

Um inteiro positivo."""


def calcula_mdc (n1,n2):

    if n2 == 0:
        return n1
    
    sobrou = n1 % n2
    n1 = n2
    n2 = sobrou
    
    return calcula_mdc(n1,n2)



n1 = int (input())
n2 = int (input())

resultado = calcula_mdc(n1,n2)

print (resultado)