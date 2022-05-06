"""Descrição
Janaína, estudante de Engenharia de Materiais, precisa calcular o resultado de x ao quadrado menos quatro x mais cinco (x**2 - 4*x + 5). Só que ela precisa calcular o resultado dessa fórmula para vários valores de x.

Formato de entrada

Dois números inteiros, um em cada linha:

O primeiro número (a) representa o primeiro valor de x que deve ser utilizado
O segundo número (b) representa o último valor de x que deve ser utilizado
Formato de saída

Os resultados de x**2 - 4*x + 5, para x no intervalo fechado entre a e b no domínio dos números inteiros.



OBS: os resultados serão sempre números inteiros, não é necessário realizar arredondamentos."""


valor1 = int (input())
valor2 = int (input())

for i in range(valor1,valor2+1):
    resultado_formula = ((i**2) - (4*i) +5)
    (print (resultado_formula))