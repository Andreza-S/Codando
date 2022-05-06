"""Descrição
O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.

Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática, e ter nota igual ou superior a 7 na redação.

Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em português e em matemática, e também a nota na redação, e depois exiba quantos candidatos foram aprovados.

Formato de entrada

Dois números inteiros seguidos por um número real para cada candidato

A entrada deve encerrar quando a quantidade de questões de português informada for inferior a zero

Formato de saída

Um número inteiro"""



qtd_alunos_aprovados = 0

while True:

    q_port = int (input()) #n de questoes certas
    if (q_port < 0):
            break
    else:
        q_mat = int (input()) #n de questoes certas
        n_red = float (input()) #nota redacao

        porcentagem_port = ((80/100) * 50)
        porcentagem_mat = ((60/100) * 35)
        NOTA_MINIMA_RED = 7
    
    if (q_port >= porcentagem_port )and (q_mat >= porcentagem_mat) and (n_red >= NOTA_MINIMA_RED): #para ser aprovado
        qtd_alunos_aprovados += 1
    else:
        pass

print (qtd_alunos_aprovados)