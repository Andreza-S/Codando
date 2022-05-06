"""Descrição
Leia duas strings e imprima "IGUAIS" caso elas sejam iguais e "DIFERENTES" caso sejam diferentes.

Formato de entrada

Você receberá duas linhas, cada uma contendo uma string com no máximo 50 caracteres.

Formato de saída

Você deve imprimir uma linha contendo a string "IGUAIS" ou "DIFERENTES"."""


palavra_1 = input()
palavra_2 = input()

if (palavra_1 == palavra_2):
    print ("IGUAIS")
else:
    print ("DIFERENTES")