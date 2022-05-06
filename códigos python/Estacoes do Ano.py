"""Descrição
As quatro estações do ano variam de acordo com as datas:

Primavera: 21 setembro até 20 dezembro
Verão: 21 dezembro até 20 março
Outono: 21 março até 20 junho
Inverno: 21 junho até 20 setembro

Escreva uma função chamada EstacaoAno que receba como entrada um dia e um mês e retorne o nome da estação correspondente.

Formato de entrada

Dois valores inteiros, representando o dia e o mês nessa sequência

Formato de saída

Um String em letras maiúsculas

Obs: Não use acento em VERAO"""


def EstacaoAno (analisar):

    if(analisar[1] == 9 or analisar[1] == 10 or analisar[1] == 11 or analisar[1] == 12): # Primavera
        if (analisar != [20,9] and (analisar != [21,12])):
            print ("PRIMAVERA")
            exit() 
    
    if(analisar[1] == 12 or analisar[1] == 1 or analisar[1] == 2 or analisar[1] == 3): # VERAO
        if (analisar != [20,12] and (analisar != [21,3])):
            print ("VERAO")
            exit()   
    if(analisar[1] == 6  or analisar[1] == 3 or analisar[1] == 4 or analisar[1] == 5): # Outono
        if (analisar != [20,3] and [21,6]):
            print ("OUTONO")
            exit()
    if(analisar[1] == 6 or analisar[1] == 7 or analisar[1] == 8 or analisar[1] == 9): # Inverno
        if (analisar != [20,6] and [21,9]):
            print ("INVERNO")
            exit()

dia = int (input())
mes = int (input())

verificar = [dia, mes]

EstacaoAno(verificar)