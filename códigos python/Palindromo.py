"""Descrição
Um palíndromo é uma palavra ou frase que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Por exemplo, as strings "aaaaa", "1221", "bbaabb" são palíndromos, entretanto a string "chef" não é um palíndromo porque se lermos da direita para a esquerda, obtemos "fehc" que não é a mesma coisa que "chef".

Ignore as diferenças entre maiúsculas e minúsculas.

Para os casos onde é dada uma frase, você deve ignorar os espaços. Por exemplo, a frase "A base do teto desaba" é considerada um palíndromo. Ao lê-la da direita para a esquerda, você obterá: "abased otet od esab A". Perceba que, com exceção do espaço, a sequência de caracteres é a mesma da frase original.

Faça um programa que indique se uma string dada é um palíndromo ou não.

Formato de entrada

A entrada consiste de um inteiro n seguido de n strings. Cada string contém no máximo 255 caracteres.

Formato de saída

Para cada string, imprima "SIM" caso seja um palíndromo e "NAO" caso contrário."""


def verifiar_palindromo (palavra):

    palavra_formatada = ("".join(palavra).lower())
    palavra_invertida = (palavra_formatada[::-1])

    if (palavra_formatada == palavra_invertida):
        print ("SIM")
    else:
        print ("NAO")

    return (palavra_invertida)


numero_de_palavras = int (input())

for i in range (numero_de_palavras):
    palavra_analisar  = input().split()

    analise = verifiar_palindromo(palavra_analisar)