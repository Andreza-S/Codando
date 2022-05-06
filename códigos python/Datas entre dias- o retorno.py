"""Descrição
Dado um array de números inteiros, seu trabalho deve ser encontrar quais elementos do array original continuam na mesma posição depois que o array for ordenado e qual é sua posição.

Exemplo:

Array original: 3, 2, 4, 10, 9, 11.

Array ordenado: 2, 3, 4, 9, 10, 11.

Número 4, posição 3

Número 11, posição 6

Formato de entrada

Um número N representando a quantidade de elementos do vetor e um vetor de números inteiros. (0 < n < 1000)



Formato de saída

A quantidade de elementos que manteve sua posição depois da ordenação do vetor e esses elementos junto com sua posição no vetor."""


n_elementos = int (input())
lista_original = input().split()

lista_original = list(map(int, lista_original))

lista_original_copia = list(map(int, lista_original))

lista_original_copia.sort()
lista_ordenado = lista_original_copia

n_manteve_posicao = 0
manteve = []
posicao = []



for i in range (len(lista_original)):
    if (lista_original[i] == lista_ordenado[i]):
        n_manteve_posicao += 1
        manteve.append (lista_original[i])
        posicao.append (i)

print (n_manteve_posicao)

for j in range (len(manteve)):
    print("{} {}".format (manteve[j], (posicao[j]+1)))