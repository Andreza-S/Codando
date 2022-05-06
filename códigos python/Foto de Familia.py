"""Descrição
Ambrosina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 04 pessoas. Tudo isso porque Ambrosina tem uma mania esquisita de ordenação. Para ela, a pessoa mais baixa deve ficar sempre do lado esquerdo, a segunda mais baixa do lado direito, no meio, logo após a mais baixa, fica a terceira mais baixa e em seguida a mais alta.
Abaixo segue uma ilustração de uma foto tirada por Ambrosina:



Formato de entrada

A entrada consiste de 04 números reais maiores que zero correspondendo às alturas de 04 pessoas. Cada número é dado em uma linha diferente. A entrada pode não estar ordenada.

Formato de saída

Consiste de 04 números reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. Os números devem ser formatados com 02 casas decimais."""


N_NUMEROS = 4

primeiro_menor = 0 #extremo da esquerda
intermedia_terc_menor = 0 #fica a direita do primeiro menor
maior = 0 # fica a direita do intermediario
segundo_menor = 0 #extremo da direita

lista = []


for i in range (N_NUMEROS):
    numero = float (input())
    lista.append(numero)


lista.sort()
lista_crescente = lista

for g in range (N_NUMEROS):
    if (g == 0):
        primeiro_menor = lista_crescente[0]
    if (g == 1):
        segundo_menor = lista_crescente[1]
    if (g == 2):
        intermedia_terc_menor = lista_crescente[2]
    if (g == 3):
        maior = lista_crescente[3]

lista_final = [primeiro_menor, intermedia_terc_menor, maior, segundo_menor]

for j in range (len(lista_final)):
    print ("{:.2f}".format (lista_final[j]))