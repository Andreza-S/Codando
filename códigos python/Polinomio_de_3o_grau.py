"""Descrição
Faça um programa que, dados os coeficientes de um polinômio de 3o. grau, resolva o polinômio para qualquer valor de x dado.

A leitura dos coeficientes vai do de maior grau para o de menor.



Formato de entrada

Os 4 coeficientes do polinômio e o valor de x a ser calculado. A leitura dos coeficientes começa pelo coeficiente de maior grau para o de menor grau.

Tantos os coeficientes quanto o valor de x podem ser compreendidos no seguinte intervalo: [-10; 10].

Formato de saída

O valor resultante da aplicação de x sobre o polinômio de acordo com os coeficientes dados."""


c1 = int (input())
c2 = int (input())
c3 =  int (input())
c4 =int (input())
Vx =  int (input())
ResultadoDoPolinomio3grau = (c1*(Vx**3)) + (c2*(Vx**2)) + (c3*Vx) + c4
print (ResultadoDoPolinomio3grau)