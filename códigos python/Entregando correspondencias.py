"""Descrição
Luíz Carlos é um carteiro muito comprometido com seu trabalho. Ele participou de uma reunião recente em que foi informado de que deveria entregar pelo menos 100 correspondências por dia para dar conta do grande fluxo de envios na época de Natal.

Escreva um programa que receba como entrada a quantidade de correspondências entregues por ele em cada um dos sete dias da semana, e exiba em quantos dias ele cumpriu a meta, e a média de entregas diárias que ele fez no período.

 

Formato de entrada

Valores inteiros

Formato de saída

Um valor inteiro para a quantidade de dias, e outro valor inteiro para a média de entregas"""


total_cartas = 0
total_dias = 0
dias_da_semana = 7
meta_entrega = 100 #cartas por dia

for i in range (dias_da_semana):
    qtd_cartas_do_dia_recebidas = int (input())

    if (qtd_cartas_do_dia_recebidas >= 100):
        total_dias += 1
    
    total_cartas += qtd_cartas_do_dia_recebidas
    media_de_entrega_por_dia = (total_cartas//dias_da_semana)

    
print (total_dias)
print (media_de_entrega_por_dia)