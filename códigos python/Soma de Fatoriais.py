"""Descrição
Escreva um programa que receba como entrada 5 números inteiros positivos, e exiba a soma dos fatoriais daqueles que são múltiplos de 3.

Formato de entrada

Números inteiros

Formato de saída

Um número inteiro"""


def fatorial (n):
   
    if n == 1:
        return 1
    
    return n * fatorial(n-1)
    
    
            
N_ENTRADAS = 5
resultado = 0

for recebe in range(N_ENTRADAS):
    numero = int (input())
   
    if (numero % 3 == 0):
        termo = fatorial(numero)
        resultado += termo
    else:
        pass

print (resultado)
