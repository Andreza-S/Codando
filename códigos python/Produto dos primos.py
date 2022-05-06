"""Descrição
Dados 04 números inteiros, calcule o produto entre eles caso os 04 números digitados sejam números primos.

Se algum deles não for primo, imprima: SEM PRODUTO

Formato de entrada

4 números inteiros

Formato de saída

O resultado da multiplicação entre eles, caso os 04 sejam primos ou SEM PRODUTO, caso contrário."""


def ProdutosPrimos (numeros):

    produto = 1

    for i in range (len(numeros)):
        primo = True

        if (numeros[i] == 1 or numeros[i] == -1 or numeros[i] == 0):
            primo = False
        else:
            if (numeros[i] % 2 == 0 and numeros[i] != 2): #divisil por2
                primo = False
            if (numeros[i] % 3 == 0 and  numeros[i] != 3): #divisil por3
                primo = False
            if (numeros[i] % 4 == 0 and numeros[i] != 4): #divisil por 4
                primo = False
            if (numeros[i]% 5 == 0 and numeros[i] != 5): #divisivel por 5
                primo = False
            if (numeros[i] % 6 == 0 and numeros[i] != 6): #divisil por 6
                primo = False
            if (numeros[i] % 7 == 0 and numeros[i] != 7): #divisivel por 7
                primo: False
            
        if (primo == False):
            print ("SEM PRODUTO")
            exit()
        else:
            produto = (produto * numeros[i])
    
    print (produto)

numeros = input().split()

numeros = list(map(int,numeros))

ProdutosPrimos(numeros)