"""Descrição
Faça um programa que encontre o divisor mais frequente d de um número x, e quantas n vezes d o divide. O divisor mais frequente é o número que pode dividir mais vezes o número x.

Se houver dois números que dividem x a mesma quantidade de vezes, então imprima o menor deles.

Exemplo: o divisor mais frequente de 12 é 2, pois o divide 2 vezes.

(Observação: Apenas divisores maiores ou iguais a 2 serão considerados.)

Formato de entrada

A entrada é um inteiro contendo o número x.

2 <= x <= 1000000

Formato de saída

A saída deve seguir o seguinte formato: "mostFrequent: d, frequency: n", onde d e n são especificados na descrição."""


n = int (input())

divisor = 0

mais_frequente = 0
frequencia = 0

for i in range (2, n+1):
    d = 0
    copia_n = n
    while copia_n % i == 0:
        copia_n = copia_n // i
        d += 1
    if d > frequencia:
        frequencia = d
        mais_frequente = i

print ("mostFrequent: {}, frequency: {}". format (mais_frequente, frequencia)) 