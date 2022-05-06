"""Descrição
A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo que calcule a multiplicação de dois inteiros. Você só poderá usar o operador soma.

Formato de entrada

Dois números inteiros.

Formato de saída

Um número inteiro representando a soma sucessiva."""


def SomaSucessivas (numero, multiplica):

    total_soma = 0

    if multiplica > 0:

        for i in range (multiplica):
            total_soma += numero

    else:
        for i in range (numero):
            total_soma += multiplica

    print (total_soma)


numero = int (input())
multiplica = int (input())

SomaSucessivas(numero, multiplica)