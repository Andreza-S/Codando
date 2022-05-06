"""Descrição
Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores positivos, o menor  valor lido, o valor delta e a soma de todos os elementos que não estão na diagonal principal.

O delta é igual a 1 se o menor valor for par e 0 se for ímpar.

Formato de entrada

9 valores inteiros referentes aos elementos da matriz.

Formato de saída

4 valores numéricos: o primeiro é um número em ponto flutuante de duas casas decimais e os outros três inteiros."""


import sys

QTD_LINHAS = 3
QTD_COLUNAS = 3

qtd_valores_positivos = 0

DELTA_MENORVALOR_PAR = 1
DELTA_MENORVALOR_IMPAR = 0

soma_valores_positivos = 0

menor_valor = sys.maxsize
soma_valores_nao_diagonoalPrincipal = 0

matriz = []

for i in range (QTD_LINHAS):
    linha = []
    for j in range (QTD_COLUNAS):
        valor = int (input())

        if (i != j):
            soma_valores_nao_diagonoalPrincipal += valor
        if (valor > 0):
            qtd_valores_positivos += 1
            soma_valores_positivos += valor
        if (valor < menor_valor):
            menor_valor = valor

        linha.append(valor)

    matriz.append(linha)

media_valores_positivos = (soma_valores_positivos / qtd_valores_positivos)

delta_final = 0

if ((menor_valor / 2) == 0 ):
    delta_final = DELTA_MENORVALOR_PAR
else:
    delta_final = DELTA_MENORVALOR_IMPAR

print ("{:.2f} {} {} {}".format (media_valores_positivos, menor_valor, delta_final, soma_valores_nao_diagonoalPrincipal))