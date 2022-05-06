"""Descrição
Escreva um programa que receba como entrada 5 números e exiba aquele cuja soma dos divisores é a maior.

Ex: A soma dos divisores de 4 é 7 (1 + 2 + 4), enquanto a soma dos divisores de 5 é 6 (1 + 5)

Formato de entrada

Cinco números inteiros

Formato de saída

Um número inteiro"""


soma_antes = 0
soma_depois = 0

N_maior = 0
soma_maior = 0

for repeticoes in range(5):
    n = int (input())   
    
    for i in range(1,n+1):

        if (n % i == 0):
            soma_depois += i
        else:
            pass
        if (i > n):
            break
     
    if (soma_depois > soma_antes):
        soma_antes = soma_depois
        soma_maior = soma_depois
        N_maior = n
        soma_depois = 0

    else:
        soma_depois = 0

print (N_maior)   