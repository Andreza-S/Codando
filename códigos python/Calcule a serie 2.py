"""Descrição
Escreva um programa que calcule os N termos da série S :

S = (1/4) + 1 + (3/8) + 1 + (5/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.

Formato de entrada

Um valor N que representa a quantidade de termos da série.

Formato de saída

Os termos da série e o valor da soma com precisão de 2 casas decimais."""


n = int (input())

CONSTANTEn1 = 2
CONSTANTEn2 = 4
CONSTANTE1 = 1

n1divisao = 1 #primeiro numeor da divisao
n2divisao = 4 #segundo numeor da divisao

termos = ""

soma1 = 0 #soma total de 1

somandodivisores = 0



for i in range (1,n+1):
    if (i == 1):
        termos += str (n1divisao) + "/" + str (n2divisao) + " "
        somandodivisores += (n1divisao/n2divisao)
    else:

        if (i % 2 == 0) and (i != n):
            soma1 += 1
            termos += "+ " + str(CONSTANTE1) + " + "
        if (i % 2 == 0) and (i == n):
            soma1 += 1
            termos += "+ " + str(CONSTANTE1) + "  "



        if (i % 2 > 0):
            n1divisao += CONSTANTEn1
            n2divisao += CONSTANTEn2
            termos += str (n1divisao) + "/" + str (n2divisao) + " "
            somandodivisores += (n1divisao/n2divisao)

sfinal = (somandodivisores + soma1)

print ("{:.2f}".format (sfinal))
print(termos)
