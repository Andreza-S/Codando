"""Descrição
Em uma escola, um professor deve realizar três avaliações por semestre. Para o cálculo da nota final, ele pode usar três diferentes métodos de cálculo de médias:

Média aritmética ("a");

Média ponderada ("p"): nesse caso, o programa deve perguntar também os pesos de cada nota;

Média harmônica ("h"): pode ser definida pela quantidade de notas dividida pela soma do inverso de cada nota. Ex.: Se as notas forem 10, 7 e 5, a média harmônica será 3/(1/10+1/7+1/5)

Faça um programa que calcula as três médias para um conjunto de 3 notas. Na saída também deve ser identificado a qual média cada valor se refere.
Formato de entrada

Três notas entre 1 e 100 cada uma e os pesos (entre 1 e 10) para o cálculo da média ponderada.

A nota mínima é 1 para não dar erro de divisão por zero com a média harmônica.

Formato de saída

As médias aritmética, ponderada e harmônica."""


n1 = int(input())
n2 = int(input())
n3 = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
mediaAritimetica = (n1+n2+n3)/3
mediaPonderada = (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
mediaHarmonica = 3/(1/n1 + 1/n2 + 1/n3)
print("a: {:.1f}" . format(mediaAritimetica))
print("p: {:.1f}". format(mediaPonderada))
print("h: {:.1f}" . format(mediaHarmonica))