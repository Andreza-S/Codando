"""Descrição
Escrever um algoritmo que lê 5 valores para "a", um de cada vez, e conta quantos destes são negativos, escrevendo esta informação.

Formato de entrada

Os 5 valores digitados.

Formato de saída

A quantidade de números negativos digitados."""

contador = 0


for i in range (0,5):
    valor = float (input ("Digite um valor:\n"))
    if (valor < 0):
        contador += 1
    else:
        pass

print ("Foram digitados {} numeros negativos".format (contador))