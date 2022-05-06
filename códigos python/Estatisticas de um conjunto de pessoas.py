"""Descrição
Escreva um programa que leia o sexo e o salário de 10 pessoas e calcule:

-       a quantidade de homens;

-       a quantidade de mulheres;

-       a média do salário de homens e de mulheres;

-       o sexo da pessoa com o maior salário;

-       a média de salário dos homens;

Formato de entrada

O sexo ('m' ou 'f') e o salário (float maior que zero) de 10 pessoas separados linha a linha.

Formato de saída

Nessa ordem:

a quantidade de homens;
a quantidade de mulheres;
a média do salário de homens e de mulheres (com precisão de 2 casas decimais);
o sexo da pessoa com o maior salário;
a média de salário dos homens (com precisão de 1 casa decimal);"""


qtd_HOMENS = 0
qtd_MULHERES = 0

media_SALARIOS = 0

maior_salario = 0
sexo_maior_salario = ""

media_HOMENS = 0

QTD_PESSOAS = 10

soma_salarios = 0
soma_salario_HOMENS = 0


for i in range (1,QTD_PESSOAS+1):
    salario = float (input())
    sexo = input() 


   
    soma_salarios += salario
    calculo_media_SALARIOS = (soma_salarios/i)
    media_SALARIOS = calculo_media_SALARIOS

    if (sexo == "m"):
        qtd_HOMENS += 1
        soma_salario_HOMENS += salario
        calculo_media_salario_HOMENS = (soma_salario_HOMENS/qtd_HOMENS)
        media_HOMENS = calculo_media_salario_HOMENS

    else:
        qtd_MULHERES += 1
    
    if (salario > maior_salario):
        maior_salario = salario
        sexo_maior_salario = sexo
    else:
        pass

print (qtd_HOMENS)
print (qtd_MULHERES)
print ("{:.1f}".format (media_SALARIOS))
print (sexo_maior_salario)
print ("{:.1f}".format (media_HOMENS))