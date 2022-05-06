"""Descrição
Luigi ganhou uma mochila nova com capacidade para transportar até 18 kg. Como tem muitos livros, ele deseja descobrir quantos podem ser levados na mochila sem exceder esse limite.

Escreva um programa que receba como entrada o peso de vários livros de Luigi e exiba a quantidade de livros que podem ser carregados.

Formato de entrada

Vários números reais representando os pesos dos livros.


Dica: a entrada deve parar quando um novo livro exceder a capacidade da mochila.

Formato de saída

Um valor inteiro"""


kg_mochila = 18
kg_atual = 0
qtd_livros = 0

while True:
    peso_livro = int (input())
    kg_atual += peso_livro

    if (kg_atual < kg_mochila):
        qtd_livros += 1
    else:
        break


print (qtd_livros)