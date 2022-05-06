"""Descrição
Na matemática é comum o uso de matrizes de números. Estas matrizes podem ser utilizadas para vários fins e a álgebra linear fornece a teoria necessária à sua manipulação.

Dada uma matriz 4 X 4, você deve fazer um programa para ler uma constante k, ler a matriz e escrevê-la após ter multiplicado os elementos da diagonal principal pela constante k.

Formato de entrada

- Um inteiro k

- 16 inteiros, correspondendo aos elementos da matriz.

Primeiro serão fornecidos os elementos da primeira coluna, depois da segunda e assim por diante até a quarta.

A entrada termina quando k for igual a 0

Formato de saída

Você deverá imprimir a matriz resultante no formato de matriz, onde os elementos da primeira linha aparecerão lado a lado, separados por um espaço (deve haver inclusive um espaço depois do último elemento de cada linha).


Cada linha da matriz será separada por um final de linha, inclusive depois da última."""


linhas = 4

while True:
    numero = int (input())
    if (numero == 0):
        break
    
    else:
        matriz = []

        for i in range (linhas):
            matriz.append([])
            for j in range (linhas):
                matriz[i].append(0)

        for t in range (linhas):
            for h in range (linhas):
                if (t == h):
                    matriz[h][t] = int (input())*numero
                else:
                    matriz[h][t] = int(input())

        for z in range (linhas):
            for x in range (linhas):
                print (matriz[z][x], end = " ")
            print()