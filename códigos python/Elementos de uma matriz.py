"""Descrição
Com o aumento do uso dos computadores a teoria das matrizes está cada vez mais sendo aplicada em áreas como, Engenharia, Matemática, dentre outras.

Assim o desafio é você criar um programa que peça ao usuário a quantidade de linhas e colunas de uma matriz que ele quer. Em seguida, inserir os elementos da matriz e imprimir a saída esperada.

Formato de entrada

A entrada consiste em uma string de dois números inteiros que indicam o número de linhas (L) e o de coluna (C), onde 0 ≤ L ≤ 100 e 0 ≤ C ≤ 100. Logo em seguida cada valor da matriz.


Formato de saída

Você deverá imprimir a matriz resultante no formato de matriz, onde os elementos da primeira linha aparecerão lado a lado, separados por um espaço (não deverá haver um espaço depois do último elemento de cada linha), a soma da sua diagonal principal e secundária e os elementos menores e maiores que zero.

OBS.: Cada linha da matriz será separada por um final de linha, inclusive depois da última. Além disso se a matriz dada não for quadrada você não poderá determinar as somas da sua diagonal principal e secundária. Verifique os exemplos!!"""


n1, n2 = input().split()

n_L = int (n1) #n de linhas
n_C = int (n2) #n de colunas

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0
qtd_numero_menor_que_0 = 0
qtd_numero_maior_que_0 = 0


matriz = []

for i in range (n_L):
    linha_termos = []
    for j in range (n_C):
        termo = int (input( ))
        linha_termos.append(termo)   

    matriz.append(linha_termos)
    
print ("Matriz formada:")

for k in range (len(matriz)):

    if (n_C == n_L):
        if (k == 0):
            soma_diagonal_secundaria += matriz[k][-1] #soma diagonal secundaria
        else:
            novo_indice = (k - (k*2) -1)
            soma_diagonal_secundaria += matriz[k][novo_indice]
    

    for g in range (len(matriz[k])):

        if (matriz[k][g] < 0):
            qtd_numero_menor_que_0 += 1
        
        if (matriz[k][g] > 0):
            qtd_numero_maior_que_0 += 1


        if (n_C == n_L):
            if (k == g):
                soma_diagonal_principal += matriz[k][g] #soma diagonal principal
            
        if (g < (n_C -1)):   
            print (matriz[k][g], end = " ")
        else:
            print (matriz[k][g])


if (n_C == n_L):
    print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.".format (soma_diagonal_principal, soma_diagonal_secundaria))
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")


print("A matriz possui {} numero(s) menor(es) que zero.".format (qtd_numero_menor_que_0))
print("A matriz possui {} numero(s) maior(es) que zero.".format (qtd_numero_maior_que_0))