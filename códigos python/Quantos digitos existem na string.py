"""Descrição
Você irá receber uma string contendo letras e dígitos. Sua missão é imprimir a quantidade de dígitos que aparecem na string.

Formato de entrada

Uma linha com até 200 caracteres contendo letras e números

Formato de saída

Uma linha contendo um número inteiro indicando a quantidade de dígitos encontrados."""


def DigitosNaString (string):

    digitos_lista = ["0","1","2","3","4","5","6","7","8","9"]

    qtd_digitos = 0

    for i in range (len(string)):
        for t in range (len(digitos_lista)):
            if (string[i] == (digitos_lista[t])):
                qtd_digitos += 1
    
    print (qtd_digitos)



string = input()

DigitosNaString(string)