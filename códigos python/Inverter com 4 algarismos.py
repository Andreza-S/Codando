"""Descrição
Faça um programa que inverta um número inteiro com quatro algarismos.

Formato de entrada

Você receberá um único número inteiro com quatro algarismos.

Formato de saída

Você deve imprimir o número invertido seguido de um final de linha.

Importante: se o número dado for 3000 por exemplo, o invertido dele deve ser 3 e não 0003."""

numero = int(input())

def inverta_numero (valor):

    valor = str (valor)

    numero_invertido = (valor[::-1])

    numero_final = []

    for i in range (len(numero_invertido)):
        if numero_invertido[i] != "0":
            numero_final.append(numero_invertido[i])
            
        if (i != 0 and numero_invertido[i] == "0"):
            if (numero_invertido[i-1] != "0"):
                numero_final.append(numero_invertido[i]) 

    numero_final = "".join(numero_final)
    numero_final = int (numero_final)

    return numero_final

invertido = inverta_numero(numero)

print(invertido)