"""Descrição
Escreva um programa que leia um valor qualquer e informe se ele é múltiplo de 5.

Dica: Use o operador "resto da divisão".

Formato de entrada

Um valor inteiro.

Formato de saída

"Eh multiplo de 5" se o valor de entrada for múltiplo.
"Nao eh multiplo de 5" se o valor de entrada não for múltiplo."""


Num = int (input())
Resto = Num % 5
if (Resto == 0 or Resto == 5):
    print ("Eh multiplo de 5")
else:
    print ("Nao eh multiplo de 5")