"""Descrição
Você deve ler uma sequência de caracteres e imprimir na ordem inversa da leitura.

Formato de entrada

Consiste de um inteiro n, indicando quantos caracteres devem ser lidos e uma sequencia de n caracteres. A entrada termina quando n=0.

Considere que n é sempre n<=100000.

Formato de saída

n caracteres impressos na ordem inversa"""


while True:
    numer_de_caracteres = int (input())
    if numer_de_caracteres == 0:
        break

    caracteres = input()
    caracteres_invertidos = []

    posicao = -1

    for i in range (len(caracteres)):
        caracteres_invertidos.append(caracteres[posicao])
        posicao += -1
    
    caracteres_invertidos = "".join(caracteres_invertidos)

    print (caracteres_invertidos)