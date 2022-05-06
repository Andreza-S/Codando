"""Descrição
Em um treino de salto em altura, cada atleta tem direito a dar um número N de saltos como parte de uma atividade prática. Faça um programa que recebe o número de atletas e quantos saltos cada atleta pode dar no início da seção. Você também deve receber a altura dos saltos de cada atleta.

No final, você deve imprimir em ordem alfabética os nomes dos atletas e a média dos saltos.

Formato de entrada

Para cada atleta:

Seu nome
Vários valores de saltos (float), informado pelo usuário.
Formato de saída

Em ordem alfabética:

O nome do atleta e a média de saltos (com uma casa decimal de precisão)."""


n_atletas = int (input())
n_saltos = int (input())

lista_atletas_e_medias = []

for i in range (n_atletas):
    nome = input()
    nome_print = (nome + ": ") #nome para impressao e concatenacao em lista
   
    soma_altura = 0
    for j in range (n_saltos): #calculo da media e recebimento das alturas

        altura = float (input())
        soma_altura += altura
    
    media = 0
    if (soma_altura > 0):
        calculo_media = (soma_altura/n_saltos)
        media = calculo_media
    
    media_str = ("{:.1f}".format (media))
    
    nome_print_e_media = (nome_print + media_str) #nome e media formatados para o print e ordenacao

    lista_atletas_e_medias.append(nome_print_e_media)

lista_atletas_e_medias.sort()

for k in range (len(lista_atletas_e_medias)):
    print(lista_atletas_e_medias[k])
