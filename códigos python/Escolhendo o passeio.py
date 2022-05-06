"""Descrição
No próximo fim-de-semana, Cristina vai sair com seus 6 primos, mas eles ainda não resolveram se vão ao cinema ou ao boliche. Escreva um programa que receba como entrada o passeio escolhido por cada um e exiba ao final aquele que teve mais votos.

Formato de entrada

Strings contendo as palavras cinema ou boliche

Dica: lembre-se que o usuário pode digitar essas palavras usando maiúsculas e/ou minúsculas


Formato de saída

Um String com o nome do passeio escolhido, sendo todas as letras maiúsculas"""


Contador = 0
Cinema = 0
Boliche = 0

while True:
    Escolha = input().lower() 

    if (Contador < 7):
        if Escolha == ("cinema"):
            Cinema += 1
            Contador += 1

        if Escolha == ("boliche"):
            Boliche += 1
            Contador += 1

    if (Contador == 7):
        if (Cinema > Boliche):
            print ("CINEMA")
            break
        else:
            print ("BOLICHE")
            break