"""Descrição
Escreva um programa que leia a idade de uma pessoa e informe quantos segundos ela viveu.

Obs: Considere que um ano sempre tem 365 dias.

Formato de entrada

A idade de uma pessoa em anos.

Formato de saída

A mesma idade conertida para segundos."""


idade = float(input())
quantidadedediasnoano = 365
segundosemumminuto = 60
segundosemumahora = 60*60
segundosemumdia = 24*segundosemumahora
segundosemumano = quantidadedediasnoano*segundosemumdia
print ("{:.0f}".format(segundosemumano*idade))