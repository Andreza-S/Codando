"""Descrição
Em uma escola, um professor deve realizar três avaliações por semestre. Para o cálculo da nota final, ele pode usar três diferentes métodos de cálculo de médias:

Média aritmética ("a");

Média ponderada ("p"): nesse caso, o programa deve perguntar também os pesos de cada nota;

Média harmônica ("h"): pode ser definida pela quantidade de notas dividida pela soma do inverso de cada nota e informa a situação dos alunos. Ex.: Se as notas forem 10, 7 e 5, a média harmônica será 3/(1/10+1/7+1/5);

Faça um programa que calcula uma das três médias para um conjunto de 3 notas. O usuário deve também informar (por meio de um único caractere) qual média ele gostaria de usar.
Formato de entrada

Um caractere que indica qual o tipo de média que será usada ("a", "p" ou "h")
Três notas do tipo inteiro (entre 1 e 100)
Três pesos (também inteiros entre 1 e 100), caso a média escolhida seja a ponderada
Formato de saída

Se o usuário digitar um caractere inválido para identificar a média emita uma mensagem de erro (sem acentos):
"Escolha um tipo de media valida."
O valor da média
A situação do aluno de acordo com sua média
"Aprovado", se a média estiver no intervalo [70; 100]
"Reprovado", se a média estiver no intervalo [0; 40] 
"Final", se a média estiver no intervalo (40; 70).
"Média inválida" em qualquer outro caso."""



TipoM = input ()

if (TipoM != "p" and TipoM != "a" and TipoM != "h"):
    print ("Escolha um tipo de media valida.")
else:
    N1 = int (input ())
    N2 = int (input ())
    N3 = int (input ())
    Ma = ( (N1 + N2 + N3) /3 )
    Mp = 0.0
    Mh = (3/ ((1/N1) + (1/N2) + (1/N3)  ))
    MediaFINAL = 0.0
    Situacao = ""
    if (TipoM == "p"):
        p1 = int (input ())
        p2 = int (input ())
        p3 = int (input ())
        Mp = (((N1 * p1) + (N2 * p2) + (N3 * p3)) / (p1 + p2 + p3))
        MediaFINAL = Mp

    if (TipoM =="a"):
        MediaFINAL = Ma

    if (TipoM =="h"):
        MediaFINAL = Mh

    if (MediaFINAL >= 70 and MediaFINAL <= 100 ):
        Situacao = "Aprovado"
    elif (MediaFINAL > 0 and MediaFINAL <= 40 ):
        Situacao = "Reprovado"
    elif (MediaFINAL >= 40 and MediaFINAL < 70 ):
        Situacao = "Final"

    if (MediaFINAL < 0 or MediaFINAL > 100):
        print ("Media")

    if (MediaFINAL >= 0 or MediaFINAL <= 100):
        print ("{:.2f}".format (MediaFINAL) + "\n" + Situacao)