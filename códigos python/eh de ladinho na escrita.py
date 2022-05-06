"""Descrição
Você irá receber um número inteiro "n" e uma sequência de n números reais, um abaixo do outro.

Imprima os n números reais, na mesma sequência, porém um ao lado do outro (todos na mesma linha) usando 3 casas decimais!

Formato de entrada

Um número inteiro "n" e uma sequência de n números reais, um abaixo do outro.

Formato de saída

Imprima os n números reais, na mesma sequência, porém um ao lado do outro (todos na mesma linha) usando 3 casas decimais. Eles devem estar separados por um espaço. Não há espaço após o último número impresso."""


contador = int (input())


for i in range(contador):
    NInserido = float (input())
    
    print ("{:.3f}". format (NInserido), end = " ")
    