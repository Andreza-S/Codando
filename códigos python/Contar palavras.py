"""Descrição
Fazer um programa para ler uma string e calcular o número de palavras que ele contém. Exemplo: casa amarela, o número de palavras é 2. 

Formato de entrada

Uma string com no mínimo 1 caracter e no máximo 500.

Formato de saída

Um inteiro indicando a quantidade de palavras na string, seguido de um fim de linha."""

inserir_palvras = input()

contar_palavras = len(inserir_palvras.split() )

print (contar_palavras)