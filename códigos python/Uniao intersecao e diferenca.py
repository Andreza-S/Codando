"""Descrição
Faça um programa que receba os elementos de 2 vetores e imprima na saída a união, a interseção e a diferença entre os 2 vetores.

Formato de entrada

No começo o usuário informa 2 inteiros que determinam a quantidade de elementos dos 2 vetores. Em seguida, o usuário informa os elementos do vetor.

Formato de saída

Os conjuntos união, interseção e diferença entre os vetores de acordo com os exemplos."""


qtd_elementos_vetor_1 = int (input())
qtd_elementos_vetor_2 = int (input())
QTD_VETORES = 2

vetor_1 = []
vetor_2 = []

for i in range (qtd_elementos_vetor_1):
    elemento_vetor_1 = input()
    vetor_1.append (elemento_vetor_1)

for j in range (qtd_elementos_vetor_2):
    elemento_vetor_2 = input()
    vetor_2.append (elemento_vetor_2)


#interse��o
intersecao = []

for k in range (len(vetor_2)):
    for l in range (len(vetor_1)):
        if (vetor_1[l] == vetor_2[k]):
            intersecao.append(vetor_1[l])

#DIFERENCA



for p in range (len(intersecao)):
    retirar = intersecao[p]
    vetor_1.remove(retirar)


diferenca = vetor_1
 

#UNIAO
uniao = vetor_2 + diferenca

print (uniao)
print (intersecao)
print (diferenca)