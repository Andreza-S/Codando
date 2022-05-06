"""Descrição
Faça um programa que solicite o nome do usuário e imprima o nome em formato de escada.

Formato de entrada

Nome informado

Formato de saída

Nome deverá ser imprimido em escada"""


nome = input()

nome_pra_impressao = []

for i in range (len(nome)):
    nome_pra_impressao.append(nome[i])

    imprimir = "".join(nome_pra_impressao)
    

    print (imprimir.upper())