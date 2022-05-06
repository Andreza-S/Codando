"""Descrição
Faça um programa que calcule a área da superfície e o volume de um cilindro. Use pi = 3.14.

O valor de saída deve ser arredondado usando 2 casas decimais.

Formato de entrada

A altura e o raio (em sequência) do cilindro. Ambos os valores são reais (float)

Formato de saída

O volume e a área da superfície (em sequência) do cilindro arredondado para 2 casas decimais."""


altura = float(input())
raio = float(input())
pi=3.14
arealateral=2*pi*raio*altura
areadabase= pi*raio**2
areadasuperficie = (2*areadabase) + arealateral
volume = areadabase*altura
print ("{:.2f}". format (volume))
print ("{:.2f}". format (areadasuperficie))