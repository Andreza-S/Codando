"""Descrição
Escreva um programa que calcule a quantidade máxima de dados a ser transmitida por um usuário levando em consideração a taxa de transmissão maxima de vídeo, áudio e dados e a capacidade do canal contratado:

QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade

O valor de saída deve ser arredondado usando 2 casas decimais.

Formato de entrada

Os valores da a taxa de transmissão maxima de vídeo, áudio e dados e a capacidade do canal. O valor da capacidade do canal é sempre maior que zero.

Formato de saída

A quantidade máxima de dados a ser transmitido."""

Tvideo = float(input())
Taudio = float(input())
Tdados = float(input())
Capacidade = float(input())
QDMax = (Tvideo*5.2 + Taudio*3.4 + Tdados*1.5)/Capacidade
print ("{:.2f}".format(QDMax))