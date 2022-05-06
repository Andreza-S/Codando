"""Descrição
Alguns professores do DCX adoram tomar café e decidiram adquirir uma cafeteira especial para a sala do Departamento. A cafeteira utiliza cápsulas de café de vários sabores para preparar a bebida, e cada cápsula prepara o equivalente a duas xícaras.

As cápsulas são vendidas em caixas pequenas (10 unidades) ou grandes (16 unidades), e ficou acertado que cada professor faria a doação de quantas caixas quisesse para o grupo.

Escreva um programa que receba como entrada a quantidade e o tamanho das caixas doadas por cada um dos sete professores que compartilham a cafeteira, e exiba a quantidade total de cápsulas de café doadas, e quantas xícaras cada professor poderá beber.

Formato de entrada

Um inteiro e um String (P ou p para caixas pequenas, G ou g para caixas grandes) para cada professor

Dica: os professores farão a doação de caixas, não de cápsulas avulsas

Formato de saída

Dois valores inteiros"""


cx_G = 16 
cx_P = 10 

xicara_pcaps = 2

total_de_caps = 0

nprof = 7


for i in range (7):
    qtd_cx = int (input())
    tamanho_cx= input()

    if (tamanho_cx == "G" or tamanho_cx == "g"):
        total_de_caps += (cx_G*qtd_cx)
    
    if (tamanho_cx == "P" or tamanho_cx == "p"):
        total_de_caps += (cx_P*qtd_cx)
    
    total_de_xicaras = (total_de_caps*xicara_pcaps)
    total_xic_pprof = (total_de_xicaras/nprof)
    
print (total_de_caps)
print ("{:.0f}".format (total_xic_pprof))