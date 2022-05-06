"""Descrição
Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

Obs: o intervalo pode ser crescente ou decrescente

Formato de entrada

Dois números inteiros

Dica: os números podem ser informados em qualquer ordem (não necessariamente o primeiro será menor que o segundo)

Formato de saída

Um número inteiro"""


nA = int (input())
nB = int (input())

SOMA_POSITIVOS = 0

if (nA < nB):
    for i in range (nA, nB+1):
        if (i > 0):
            SOMA_POSITIVOS  += i
        else:
            pass

if (nB < 0):
    for i in range (nA,nB+1, -1):
        if (i > 0):
            SOMA_POSITIVOS  += i
        else:
            pass

print (SOMA_POSITIVOS)