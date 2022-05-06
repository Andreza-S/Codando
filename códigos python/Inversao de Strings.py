"""Descrição
Escreva um programa para inverter os caracteres das strings digitadas pelo usuário e imprimi-las na saída.Para isto deve-se fazer uso de uma função recursiva chamada inverter que recebe uma string como parâmetro e retorna uma string com os caracteres invertidos.

Restrição: O programa só pode utilizar 1 (um) laço. Além disso, este laço tem que ser do tipo for.

Formato de entrada

O programa deve ler a quantidade de strings que serão lidas pelo programa (N). Em cada uma das linhas seguintes o programa deve ler as N strings que serão invertidas.

Formato de saída

A saída consiste de N linhas contendo as strings invertidas."""


def inverta_string (palavra):

    palavra_invertida = (palavra[::-1])

    return palavra_invertida

numero_de_strings = int (input())

for i in range (numero_de_strings):

    palavra = input()

    impressao_invertida = inverta_string(palavra)

    print (impressao_invertida)