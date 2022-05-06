"""Descrição
Uma plataforma online oferece 4 tipos de jogos, onde Cada um desses tipos de jogo tem uma faixa etária para que o jogador possa participar.

Jogos de azar - Apostas esportivas, blackjack, roleta e afins.
21 anos ou mais
MMORPG - Massively Multiplayer Online Role-Playing Game
14 anos ou mais
MOBA - Multiplayer Online Battle Arena
10 anos ou mais
Casual
Sem limite de idade
Faça um programa que receba a idade do jogador e o tipo de jogo que ele deseja jogar e informe se ela pode jogar. Caso a idade do jogador caia fora do intervalo válido ou seja informado um tipo de jogo que não existe, deve ser emitida uma mensagem de erro de acordo com o que aconteceu.

Formato de entrada

A idade do jogador [0;130] - Caso a idade caia fora do intervalo deve ser emitida a mensagem de erro: "Idade invalida."
O tipo de jogo que o jogador quer jogar dentre as seguintes possibilidades:
azar
mmorpg
moba
casual
Caso seja informado um tipo de jogo que não existe, deve ser emitida a mensagem: "Jogo invalido"
Formato de saída

Uma frase que indica se o jogador pode jogar ou não:
"Pode entrar!" - Caso o jogador esteja apto a jogar o jogo escolhido.
"Volte daqui há alguns anos." - Caso o jogador não tenha idade para jogar o jogo escolhido.
"Jogo invalido." - Caso o jogador tenha informado um jogo que não esteja na lista.
"Idade invalida." - Caso a idade informada caia fora do intervalo válido."""


Idade = float (input())
Jogo = input()
if Jogo == "azar" and Idade >= 21:
    print ("Pode entrar!")
elif  Jogo == "azar" and Idade < 21:
    print ("Volte daqui há alguns anos.")
elif Jogo == "mmorpg" and Idade >= 14:
    print ("Pode entrar!")
elif Jogo == "mmorpg" and Idade < 14:
    print ("Volte daqui há alguns anos.")
elif Jogo == "moba" and Idade >= 10:
    print ("Pode entrar!")
elif Jogo == "moba" and Idade < 10 and Idade >0:
    print ("Volte daqui há alguns anos.")
elif Jogo == "casual" and Idade >0:
    print ("Pode entrar!")
elif Idade < 0 or Idade > 130:
    print ("Idade invalida.")
elif Jogo != ("azar") or Jogo != ("mmorpg") or Jogo != ("moba") or Jogo != ("casual"):
    print ("Jogo invalido.") 