"""Descrição
Calcule a velocidade média das moléculas de um gás a partir dos seguintes parâmetros:

Temperatura do gás em Kelvin (0.0 até 200.0)
A massa molar do gás (1.0 até 200.0)
A constante universal dos gases perfeitos (8.31)
O valor de saída deve ser arredondado usando 2 casas decimais.

Pesquise como fazer a operação de raiz quadrada.

Formato de entrada

A temperatura do gás em Kelvin. (0.0 até 200.0)
Sua massa molar. (1.0 até 200.0)
Formato de saída

A velocidade média das moléculas de um gás."""


TemperaturaK = float (input())
MassaM = float (input()) 
ConstanteU = 8.31
Xv = ((ConstanteU*TemperaturaK)*3) / MassaM
X2v = (Xv**0.5)
print ("{:.2f}".format (X2v))