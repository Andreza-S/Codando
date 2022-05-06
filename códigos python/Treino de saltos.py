"""Descrição
Em um treino de salto em altura, cada atleta tem direito a dar quantos saltos quiser como parte de uma atividade prática. Faça um programa que recebe a altura dos saltos de cada atleta enquanto ele quiser saltar. Para informar que o atleta não quer mais saltar é informado um valor de salto negativo.

Seu programa deve receber o nome de cada atleta e informar qual a média de altura dos saltos para cada um. Devem ser recebidos novos atletas até que seja digitado "sair" no nome do atleta.

Formato de entrada

Para cada atleta:

Seu nome
Vários valores de saltos (float), até que seja informado um salto negativo
Formato de saída

Para cada atleta:

O nome do atleta e a média de saltos (com uma casa decimal de precisão)."""


while True:
    nome = input()

    if (nome == "sair"):
        exit()

    else:
        n_saltos = 0 
        soma_saltos = 0 
        soma_saltos = 0
        n_saltos = 0
        media = 0

        while (nome != "sair"):  
            salto = float (input())
        
            if (salto > 0):
                soma_saltos += salto
                n_saltos += 1
                media = (soma_saltos/n_saltos)

            if (salto < 0):
                print ("{}: {:.1f}".format (nome, media))
                break