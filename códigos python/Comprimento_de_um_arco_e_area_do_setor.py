"""Descrição
Calcule o comprimento do arco de uma circunferência (a curva AB na figura) e a área do seu setor (delimitado pelo arco e hachurado de cinza na figura) usando os seguintes parâmetros:

O raio da circunferência (entre 1.0 e 50.0)
A medida do ângulo em graus (entre 0.0 e 359.0)
Use pi = 3.14
O valor de saída deve ser arredondado usando 2 casas decimais.


Formato de entrada

O raio da circunferência (entre 1.0 e 50.0)

A medida do ângulo em graus (entre 0.0 e 359.0)

Formato de saída

A medida do comprimento do arco.

A área do setor."""


raio = float (input())
angulo = float (input())
pi=3.14
comprimentodearco = (raio*angulo*pi)/180
areadosetor = (angulo*pi*(raio**2))/360
print ("{:.2f}". format (comprimentodearco))
print ("{:.2f}". format (areadosetor))