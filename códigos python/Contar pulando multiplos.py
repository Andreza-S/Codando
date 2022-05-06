"""Descrição
Sempre que Mariana faz alguma trela a professora a coloca de castigo, obrigando-a a escrever centenas de números. Para se distrair um pouco durante o castigo, a Mariana inventou uma pequena brincadeira: quando vai escrever os números, ela pula todos os múltiplos de 10. Escreva um programa que reproduza esse comportamento de Mariana.

Formato de entrada

Um número inteiro positivo N

Formato de saída

Os números inteiros de 1 a N, incluindo o N.
Os números que são múltiplos de 10 não devem ser impressos.
Cada número deve estar em uma linha."""


nFinal = int (input())

for i in range (nFinal+1):
    
    if (i % 10 != 0):
        print (i)
    else:
        pass