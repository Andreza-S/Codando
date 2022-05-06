"""Descrição
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

Formato de entrada

Inteiro referente ao dia da semana

Formato de saída

O dia da semana correspondente ao número."""

NDoDia = int (input())
if NDoDia == 1:
    print ("Domingo")
elif NDoDia == 2:
    print ("Segunda")
elif NDoDia == 3:
    print ("Terça")
elif NDoDia == 4:
    print ("Quarta")
elif NDoDia == 5:
    print ("Quinta")
elif NDoDia == 6:
    print ("Sexta")
elif NDoDia == 7:
    print ("Sabado")
else:
    print ("valor invalido")