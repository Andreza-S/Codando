"""Descrição
O objetivo dessa tarefa é aprender a manipular listas em Python. Deve-se apresentar um programa que leia até 5 notas de um determinado aluno e as guarde em uma lista.

Em seguida, o programa deve exibir cada nota lida indicando sua posição na lista.

Formato de entrada

Um número inteiro n indicando o número de notas a ser lido ( 0 < n <=5).

As n notas do aluno. As notas devem ser do tipo float.

Formato de saída

O programa deve exibir cada nota com sua posição da seguinte forma:

Nota 1: 10.0

Nota 2: 9.0

Em seguida, a média das notas lidas, com duas casas decimais.

9.50

A mensagem "Número de notas inválido." deve ser exibida caso o valor de n não obedeça ao critério estabelecido."""


n_notas = int (input())
if (n_notas < 1) or (n_notas > 5):
    print ("Numero de notas invalido.")

else:
    soma_media = 0
    lista_notas = []


    for i in range (1,n_notas+1):
        nota = float (input())
        lista_notas.append(nota)
        soma_media += nota
        posicao_nota = i

        print ("Nota {}: {:.1f}".format (posicao_nota, nota))
    
    media = (soma_media/n_notas)

    print ("Media: {:.2f}".format (media))