"""Descrição
Faça um programa que receba o código da origem de um produto e informe em qual região ele foi produzido, ou seja, qual é a sua procedência. Para isso utilize a tabela abaixo que associa o código de origem à região de procedência.


Código da Origem   Região de Procedência
1                   Nordeste
2                   Norte
3 e 4               Centro-Oeste
5 a 9               Sul
10 a 15             Sudeste     

Formato de entrada

A entrada consiste de um número inteiro que corresponde ao código da origem.

Formato de saída

A saída do nome da região de origem do produto, conforme estabelecido na tabela."""


Codigo = float (input())
if Codigo == 1:
    print ("Nordeste")
elif Codigo == 2:
    print ("Norte")
elif Codigo == 3 or Codigo ==4:
    print ("Centro-Oeste")
elif Codigo == 5 or Codigo == 6 or Codigo == 7 or  Codigo == 8 or Codigo == 9:
    print ("Sul")
elif  Codigo == 10 or Codigo == 11 or Codigo == 12 or Codigo == 13 or Codigo == 14 or Codigo == 15:
    print ("Sudeste")



