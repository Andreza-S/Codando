"""Descrição
O técnico da seleção brasileira vai escalar os 11 titulares que jogarão a copa do mundo e ele precisa de você para ajudar a colher algumas estatísticas dos jogadores.

Você vai receber os nomes dos jogadores até completar os 11 ou até que o treinador digite sair no nome do jogador.

Além do nome você recebrá da entrada padrão a idade e a posição do jogador.

Em seguida você deve imprimir:

O nome do jogador mais jovem
A posição do jogador mais velho
A média de idade
Formato de entrada

Nome
Idade
Posição
(A)tacante
(M)eio-campo
(D)efensor
(G)oleiro
Formato de saída

O nome do jogador mais jovem
A posição do jogador mais velho
A média de idade com uma casa decimal de aproximação"""


soma_idade = 0
qtd_jogadores = 0
idade_mais_velha = 0
idade_mais_jovem = 0
o_nome_do_mais_jovem = ""
a_posicao_do_mais_velho = ""

for i in range (11):
    nome = input()

    if nome == "sair":
        break
    else:
        idade = int (input())
        posicao = input()

        qtd_jogadores += 1
        soma_idade += idade

    
        if idade_mais_jovem == 0:
            idade_mais_jovem = idade

        if idade > idade_mais_velha:
            idade_mais_velha = idade
            a_posicao_do_mais_velho = posicao
        
        if idade < idade_mais_jovem or idade == idade_mais_jovem:
            idade_mais_jovem = idade
            o_nome_do_mais_jovem = nome


a_media_de_idade = (soma_idade/qtd_jogadores)

print (o_nome_do_mais_jovem)
print (a_posicao_do_mais_velho)
print ("{:.1f}".format (a_media_de_idade))