"""Descrição
Faça um programa que leia um número inteiro e informe qual o mês do ano correspondente por extenso. Caso seja um mês inválido, informe ao usuario.

Formato de entrada

Você receberá um número inteiro correspondente ao mês do ano. Considere que o mês de janeiro como 1 e o mês de dezembro como 12.

Qualquer inteiro fora desse intervalo deve ser considerado como um mês inválido.

 

Formato de saída

A saída deve ser um dos meses do ano, correspondendo ao inteiro dado na entrada, seguido de um final de linha. Portanto, as possíveis saídas são:

janeiro

fevereiro

marco

abril

maio

junho

julho

agosto

setembro

outubro

novembro

dezembro

 

Caso o mês seja inválido, imprima como resposta:

invalido

 

IMPORTANTE: perceba que a saída está toda em letras minúsculas e SEM ACENTOS."""



def MesPorExtenso (mes):
    
    meses_extenso = ["0","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    if (mes > 0 and mes <= 12):
        for i in range (len(meses_extenso)):
            if (i == mes):
                print(meses_extenso[i])
                break
    else:
        print("invalido")

mes = int (input())

MesPorExtenso(mes)