"""Descrição
Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
Formato de entrada

Uma escala de medida de temperatura ("C", "F" ou "K")

Um valor de temperatura a ser convertido

Esse valor deve obedecer os seguintes valores mínimos (float):
Celsius: t >= -273.0
Fahrenheit: t >= -459,67
Kelvin: t >= 0.0
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"
Não há limite máximo de temperatura


Formato de saída

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"""


EscalaDeT = input ()
Temperatura = float (input())

ConvCemK = (Temperatura + 273.15)
ConvKemC = (Temperatura - 273.15)
ConvCemF = ((1.8*Temperatura) + 32)
ConvFemC = ((Temperatura-32) / 1.8)
ConvKemF = ((Temperatura - 273.15) * (1.8) + 32)
ConvFemK = ((Temperatura + 459.67) * 5/9)

if EscalaDeT == "C" and Temperatura >= -273.0:
    print ("{:.2f}".format (ConvCemF) + " F")
    print ("{:.2f}".format (ConvCemK) + " K")
    
elif EscalaDeT == "F" and Temperatura >= -459.67:
    print ("{:.2f}".format (ConvFemC) + " C")
    print ("{:.2f}".format (ConvFemK) + " K")

elif EscalaDeT == "K" and Temperatura >= 0.0:
    print ("{:.2f}".format (ConvKemC) + " C")
    print ("{:.2f}".format (ConvKemF) + " F")
elif Temperatura < -273.0 or Temperatura < 0.0:
    print ("Valor de temperatura abaixo do minimo")