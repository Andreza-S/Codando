"""Descrição
Faça um programa em Python que converta galões em litros. Leve em consideração que 1 galão é equivalente a 3,7854 litros.

Formato de entrada

A entrada consiste de uma linha contendo em 3 valores inteiros.

Formato de saída

A saída consiste de 3 linhas contendo a conversão de galões para litros de cada um dos 3 valores da entrada. Osvalores numéricos de cada uma das linhas devem ter 2 casas decimais."""


n1, n2, n3 = input().split()

Qtd_G1 = int (n1)
Qtd_G2 = int (n2)
Qtd_G3 = int (n3)

L_por_Galao = (3.7854)

Valor_em_LitrosV1 = (Qtd_G1 * L_por_Galao)
Valor_em_LitrosV2 = (Qtd_G2 * L_por_Galao)
Valor_em_LitrosV3 = (Qtd_G3 * L_por_Galao)

if (Valor_em_LitrosV1) > (L_por_Galao):
    print ("{} GALOES -> {:.2f} LITROS".format (Qtd_G1,Valor_em_LitrosV1))
else:
    if (Valor_em_LitrosV1) == (L_por_Galao):
        print ("{} GALAO -> {:.2f} LITROS".format (Qtd_G1,Valor_em_LitrosV1))


if (Valor_em_LitrosV2) > (L_por_Galao):
    print ("{} GALOES -> {:.2f} LITROS".format (Qtd_G2,Valor_em_LitrosV2))
else:
    if (Valor_em_LitrosV2) == (L_por_Galao):
        print ("{} GALAO -> {:.2f} LITROS".format (Qtd_G2,Valor_em_LitrosV2))

if (Valor_em_LitrosV3) > (L_por_Galao):
    print ("{} GALOES -> {:.2f} LITROS".format (Qtd_G3,Valor_em_LitrosV3))
else:
    if (Valor_em_LitrosV3) == (L_por_Galao):
        print ("{} GALAO -> {:.2f} LITROS".format (Qtd_G3,Valor_em_LitrosV3))