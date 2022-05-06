"""Descrição
Faça um programa que receba os nomes e a pontuação de vários jogadores de basquete até que o usuário digite "sair" em vez do nome de um jogador. No final, mostre:

O nome do jogador que fez a menor quantidade de pontos
O nome do jogador que fez a maior quantidade de pontos
A média dos pontos de todos os jogadores
Se não for fornecido os dados de nenhum jogador, imprima na saída: "Nenhum jogador foi registrado."

Se houver mais de um jogador com a mesma pontuação, para efeito de cálculo do jogador com maior (ou menor) quantidade de pontos, deve ser considerado o último jogador inserido. (Vide casos de teste)

Formato de entrada

Em sequência os nomes e a pontuação de vários jogadores de basquete ou "sair" para terminar o programa.

Formato de saída

Assim que o usuário digitar sair, imprima:

O nome do jogador que fez a menor quantidade de pontos
O nome do jogador que fez a maior quantidade de pontos
A média dos pontos de todos os jogadores (com duas casas decimais de aproximação)
Se não for fornecido os dados de nenhum jogador, imprima na saída: "Nenhum jogador foi registrado."""



jogador_MAIOR_ponto = ""

jogador_menor_ponto = ""

n_jodadores = 0

maior_ponto = 0
menor_PONTO = 999999999999999999999999999

soma_dos_pontos = 0

media = 0 

while True:
    nome = input()
    if (nome == "sair"):
        break
    else:
        n_jodadores += 1

        pontos = int (input())

        soma_dos_pontos += pontos

        calculo_media = (soma_dos_pontos/(n_jodadores))
        media = calculo_media

        if (pontos >= maior_ponto):
            maior_ponto = pontos
            jogador_MAIOR_ponto = nome


        if (pontos <= menor_PONTO):
            menor_PONTO = pontos
            jogador_menor_ponto = nome


if (n_jodadores == 0):
    print ("Nenhum jogador foi registrado.")
else:
    print (jogador_menor_ponto)
    print (jogador_MAIOR_ponto)
    print ("{:.2f}".format (media))