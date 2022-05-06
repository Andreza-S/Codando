"""Descrição
Faça um programa que leia 3 números inteiros e imprima o valor intermediário (entre o menor e o maior número). Suponha que os números são diferentes.

Formato de entrada

Consiste de 3 números inteiros.

Formato de saída

Consiste do número inteiro cujo valor é o intermediário entre os valores de entrada."""


N_DE_NUMEROS = 3
lista_numeros = []


for i in range (N_DE_NUMEROS):
    numero = input()
    lista_numeros.append(numero)
    
lista_inteiros = list(map(int, lista_numeros))
maior_numero = 0
numero_intermediario = 0
menor_numero = 0


for j in range (len(lista_inteiros)):
    if (j == 0):
        maior_numero = lista_inteiros[j]
        menor_numero = lista_inteiros[j]

    else:
        if (lista_inteiros[j] < menor_numero):
            menor_numero = lista_inteiros[j]
        if ( lista_inteiros[j] > maior_numero):
            maior_numero = lista_inteiros[j]

for g in range (len(lista_inteiros)):
    if ( lista_inteiros[g] > menor_numero) and ( lista_inteiros[g] < (maior_numero)):
        numero_intermediario = lista_inteiros[g]

print (numero_intermediario)