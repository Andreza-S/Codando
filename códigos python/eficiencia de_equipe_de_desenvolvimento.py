"""Descrição
Escreva um programa que leia a quantidade de linhas de um programa (QUANTL), o número de funções existente nele (QUANTF), o tamanho da equipe (TAMEQ) e o número de bugs (NUMB) encontrados e calcule a eficiência da equipe de acordo com a seguinte formula: EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2 x NUMB
Utilize uma casa decimal de aproximação.

Formato de entrada

Os quatro parâmetros que determinam a eficiência:

-Quantidade de linhas de um programa (QUANTL)
-Número de funções existente nele (QUANTF)
-Tamanho da equipe (TAMEQ)
-Número de bugs (NUMB)
-Formato de saída

O valor real (float) da eficiência."""

QUANTL = float(input())
QUANTF = float(input())
TAMEQ = float(input())
NUMB = float(input())
eficiencia = (QUANTL/QUANTF)/TAMEQ-4.2*NUMB
print ("{:.1f}".format(eficiencia))