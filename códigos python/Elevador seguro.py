"""Descrição
Genival é ascensorista da Prefeitura Municipal e todos os dias conduz os passageiros para cima e para baixo. O elevador que ele opera tem capacidade para no máximo 7 pessoas e no máximo 560 quilos.

Escreva um programa que receba como entrada o peso de várias pessoas que estão entrando no elevador e exiba quantas poderão ser transportadas com segurança e o peso total carregado, respeitando os limites do elevador.

Formato de entrada

Vários valores reais

A entrada de dados será encerrada quando for informado o valor zero, ou quando um dos limites do elevador tiver sido atingido

Formato de saída

Um valor inteiro e um valor real com uma única casa decimal"""


kgP = float (input())

total_Kg = kgP
total_P = 1

while True:
    KgP = float (input())
    
    if (KgP == 0):
        break

    if (total_Kg == 560):
        break

    if  (total_P == 7):
        break

    if (total_Kg < 560) and (total_P < 7):
        total_Kg += KgP
        total_P += 1

    

print (total_P)
print ("{:.1f}".format (total_Kg))