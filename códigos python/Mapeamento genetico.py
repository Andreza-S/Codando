"""Descrição
Identificação de cadeias de DNA é uma importante atividade na Engenharia Genética.

Nesse problema iremos identificar em uma sequência de DNA onde se localiza a maior subsequência de uma determinada base e a quantidade.

Vamos ajudar os cientistas da área a resolver esse problema! 

Formato de entrada

sequência de DNA

base a ser procurada

Formato de saída

posição onde se localiza a maior subsequência

tamanho da maior subsequência"""


def localizar_base_dna_posicao_quatidade (cadeia_dna, base):

    posicoes = []
    quantidades = []

    maior_quantidade = 0
    posicao_maior_quantidade = 0

    if base in cadeia_dna:

        for i in range (len(cadeia_dna)):
            if (cadeia_dna[i] == base):
                posicao = i
                qtd = 1
                
                for j in range (i+1,len(cadeia_dna)):
                    if (cadeia_dna[j] == base):
                        qtd += 1
                    else:
                        break

                posicoes.append (posicao)
                quantidades.append(qtd)

        if (len(quantidades) > 1):
        
            for x in range (len(quantidades)):
                if (quantidades[x] > maior_quantidade):
                    maior_quantidade = quantidades[x]
                    posicao_maior_quantidade = posicoes[x]
        else:
            maior_quantidade = quantidades[0]
            posicao_maior_quantidade = 0
        
        print (posicao_maior_quantidade)
        print(maior_quantidade)
    else:
        print ("ERRO")
cadeia_para_analise = input()
pesquise_base = input()

localizar_base_dna_posicao_quatidade(cadeia_para_analise, pesquise_base)