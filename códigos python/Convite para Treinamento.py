"""Descrição
O principal prêmio da Olimpíada de Informática é o convite para os cursos de programação oferecidos no Instituto de Computação da Unicamp, com todas as despesas pagas. São convidados apenas os competidores que atingem um certo número mínimo de pontos, consideradas as duas fases de provas.

Você foi contratado para fazer um programa que, dados os números de pontos obtidos por cada competidor em cada uma das fases, e o número mínimo de pontos para ser convidado, determine quantos competidores serão convidados para o curso na Unicamp. Você deve considerar que

todos os competidores participaram das duas fases;
o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases;
o competidor não pode zerar em nenhuma das fases.
Por exemplo, se a pontuação mínima para ser convidado é 435 pontos, um competidor que tenha obtido 200 pontos na primeira fase e 235 pontos na segunda fase será convidado para o curso na Unicamp. Já um competidor que tenha obtido 200 pontos na primeira fase e 234 pontos na segunda fase não será convidado.

Formato de entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A primeira linha da entrada contém um inteiro N, o número de competidores (1 ≤ N≤ 1000) e a segunda linha o inteiro P, o número mínimo de pontos para ser convidado (1 ≤ P≤ 1000). A seguir são lidas as informações dos N competidores: X e Y, indicando a pontuação de um competidor em cada uma das fases (0 ≤ X≤ 400) e (0 ≤ Y≤ 400).

Formato de saída

Seu programa deve imprimir na saída padrão uma única linha contendo um único inteiro, indicando o número de competidores que serão convidados a participar do curso na Unicamp"""


n_competidores = int (input())
pontos_minimos = int (input())

convidados = 0

for i in range(n_competidores):
    pontos_1_rodada = int (input())
    pontos_2_rodada = int (input())
    
    if (pontos_1_rodada > 0) and (pontos_2_rodada > 0):

        pontos_Totais_do_jogador = (pontos_1_rodada + pontos_2_rodada)
        if (pontos_Totais_do_jogador >= pontos_minimos):
                convidados += 1
                pontos_Totais_do_jogador = 0       
        else:
            pontos_Totais_do_jogador = 0
    else:
        pass


print (convidados)