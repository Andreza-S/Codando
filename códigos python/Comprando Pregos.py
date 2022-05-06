"""Descrição
Lissandra comprou vários quadros novos para seu apartamento e agora precisa de pregos para pendurá-los. Pesquisando, ela descobriu que uma caixa com 12 pregos custa R$ 7,89.

Escreva um programa que receba a quantidade de pregos necessários para cada quadro, até que seja informada uma quantidade ímpar, e exiba o valor total que será gasto e a quantidade de pregos que vão sobrar.

Formato de entrada

Vários números inteiros até que seja informado um ímpar

Formato de saída

Na primeira linha, um valor real com duas casas decimais.

Na segunda linha, um valor inteiro"""


QPC = 12
VCP = 7.89

qtde_pregos_total = 0

while True:
    qtde_pregos = int (input())
    if qtde_pregos % 2 != 0:
        break
    qtde_pregos_total += qtde_pregos

qtde_caixas = qtde_pregos_total // QPC
pregos_sobrando = 0
if qtde_pregos_total % QPC != 0:
    qtde_caixas += 1
    pregos_sobrando = QPC - qtde_pregos_total % QPC

print (qtde_caixas*VCP)
print (pregos_sobrando)