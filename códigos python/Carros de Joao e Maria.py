"""Descrição
João e Maria estão querendo obter informações sobre os carros de sua cidade.

Para isso eles pediram que você escrevesse um programa para ajudá-los. Eles vão digitar informações de diferentes carros e quando quiserem parar a leitura vão digitar a resposta n ou N.

Para cada carro serão lidos o ano e a velocidade.

O programa deve exibir a quantidade de carros, o carro mais novo e o mais rápido.


Atenção: 

- assuma que o usuário sempre vai digitar o nome do carro e da cor em minúsculos. 

Formato de entrada

Um valor inteiro (ano) e um em ponto flutuante (velocidade) 

Um caractere


Formato de saída

Maior velocidade, maior ano e velocidade média."""


caracte = input()

if (caracte == "n" or caracte == "N"):
    print ("zero")
    exit()

soma_velocidade = 0
quantidade_de_carros = 0

maior_ano = 0
maior_velocidade = 0

while (caracte != "n" or caracte != "N"):

    ano = int (input())
    velocidade = float (input())

    quantidade_de_carros += 1

    soma_velocidade += velocidade

    if (ano > maior_ano):
        maior_ano = ano

    if (velocidade > maior_velocidade):
        maior_velocidade = velocidade
    
    
    velocidade_media = (soma_velocidade / quantidade_de_carros)

    
    caracte = input()
    if (caracte == "n" or caracte == "N"):
        print ("{:.2f}".format (maior_velocidade))
        print (maior_ano)    
        print ("{:.2f}".format (velocidade_media))
        break
    
    else:
        pass


