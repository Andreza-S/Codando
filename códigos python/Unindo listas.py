"""Descrição
Faça um programa para ler duas listas de valores inteiros e gerar uma terceira lista que seja a união das duas listas informadas pelo usuário.

As listas devem ter pelo menos 1 elemento. Caso contrário, deve ser exibida a mensagem "Erro - A lista deve ter pelo menos 1 elemento."

Formato de entrada

Número de elementos da primeira lista
Valores da primeira lista (separados por uma quebra de linha)
Número de elementos da segunda lista
Valores da segunda lista (separados por uma quebra de linha)
Formato de saída

A lista contendo todos os valores da primeira lista e dos valores da segunda lista."""


N_DE_LISTAS = 2

n_lista_1 = int (input())

if (n_lista_1 == 0):
    print ("Erro - A lista deve ter pelo menos 1 elemento.")
    exit()

lista_1 = []

for i in range (n_lista_1):
    numeros_lista_1 = int (input())
    lista_1.append(numeros_lista_1)

n_lista_2 = int (input())
if (n_lista_2 == 0):
    print ("Erro - A lista deve ter pelo menos 1 elemento.")
    exit()

lista_2 = []

for j in range (n_lista_2):
    numeros_lista_2 = int (input()) 
    lista_2.append(numeros_lista_2)

lista_final = []

for g in range (N_DE_LISTAS):
    if (g == 0):
        for h in range (len(lista_1)):
            lista_final.append(lista_1[h])

    else:
        for k in range (len(lista_2)):
            lista_final.append(lista_2[k])

for l in range (len(lista_final)):
    print("{} ".format (lista_final[l]), end = "")