"""Descrição
Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

A tabela abaixo traz exemplos de entrada e saída esperadas.

Formato de entrada

2016

4

Formato de saída

2020 2024 2028"""


ano_de_vacinacao = int (input())
periodicidade = int (input())


for i in range (3):
    ano_de_vacinacao += periodicidade
    print (ano_de_vacinacao, end = " ")