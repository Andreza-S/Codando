"""Descrição
Faça um programa para determinar se 2 números primos (X e Y) somados resultam em outro número primo.

Seu programa deve receber 2 números, verificar se os 2 são primos e, caso eles sejam primos, verificar se a soma deles é primo.

Se seu programa identificar que algum número recebido não é primo, ele deve imprimir a seguinte mensagem:

"O número N não é primo."

Use uma função para fazer a impressão dessa mensagem passando o número como parâmetro.

Se a soma dos 2 números for um primo, emita a seguinte mensagem:

"A soma de X e Y é um primo."

Caso contrário, escreva a mensagem:

"A soma de X e Y não é um primo."

Formato de entrada

Dois números inteiros X e Y.

Formato de saída

Uma mensagem de erro:

"O número N não é primo."

Ou, se a soma dos 2 números for um primo, emita a seguinte mensagem:

"A soma de X e Y é um primo."

Caso contrário, escreva a mensagem:

"A soma de X e Y não é um primo."""



def eh_primo (numeros):

    soma_final = 0

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
        
        if primo == True:
            soma_final += (numeros[i])
        else:
            print ("O numero {} nao eh primo.".format (numeros[i]))
            exit()

    
    primo = True #verificando se soma � primo

    if (soma_final == 1 or soma_final == -1 or soma_final == 0):
        primo = False
    else:
        if (soma_final % 2 == 0 and soma_final != 2): #divisil por2
            primo = False
        if (soma_final % 3 == 0 and  soma_final != 3): #divisil por3
            primo = False
        if (soma_final % 4 == 0 and soma_final != 4): #divisil por 4
             primo = False
        if (soma_final% 5 == 0 and soma_final != 5): #divisivel por 5
            primo = False
        if (soma_final % 6 == 0 and soma_final != 6): #divisil por 6
            primo = False
        if (soma_final % 7 == 0 and soma_final != 7): #divisivel por 7
            primo: False

        if primo == True:
           print ("A soma de {} e {} eh um primo.".format (numeros[0], numeros[1]))
        else:
            print ("A soma de {} e {} nao eh um primo.".format (numeros[0],numeros[1]))


n1 = int (input())
n2 = int (input())

numeros = []

numeros.append(n1)
numeros.append(n2)

eh_primo (numeros)