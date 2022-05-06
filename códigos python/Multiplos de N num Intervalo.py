"""Descrição
Escrever programa para exibir os múltiplos de N contidos entre os valores A e B, sendo N, A e B definidos pelo utilizador.

Formato de entrada

Três valores inteiros.  Cada um em uma linha distinta.  O primeiro valor, N,  corresponde ao número do qual se deseja verificar se há múltiplos.  Os outros dois valores, A e B inclusivos, correspondem aos limites do intervalo de valores a serem validados como múltiplos ou não de N.

Formato de saída

Valores contidos entre A e B, que sejam múltiplos de N.

Caso não haja múltiplos de N, entre A e B, exibir: INEXISTENTE."""


n = int (input())
nInicial = int (input())
nFinal = int (input())

multiplos = False

for i in range (nInicial, nFinal+1):
    if (i % n == 0):
        print (i)
        multiplos = True
    else:
        pass

if (multiplos == False):
    print ("INEXISTENTE")