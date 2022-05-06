"""Descrição
A diagonal de um polígono é um segmento de linha que liga 2 vértices não adjacentes

Faça um programa que calcula a quantidade de diagonais de um polígono baseado na quantidade de lados desse polígono

Formato de entrada

Um valor inteiro que representa a quantidade de lados do polígono.

Formato de saída

Um valor inteiro que representa a quantidade de diagonais do polígono."""

lados = int(input())
diagonais = lados*(lados-3)/2
print ("{:.0f}".format (diagonais))