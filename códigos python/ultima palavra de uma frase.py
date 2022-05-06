"""Descrição
Leia uma string e imprima somente a última palavra da mesma. Exemplo: Se a string digitada for "José da Silva", deverá ser impresso na tela a substring "Silva".

Formato de entrada

Uma frase com no máximo 400 caracteres.

Formato de saída

Uma única linha contendo a última palavra da frase digitada."""


frase = input().split()

print (frase[-1])