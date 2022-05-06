"""Descrição
Vamos brincar com Fibonacci.
Na matemática, a Sucessão de Fibonacci (também Sequência de Fibonacci), é uma sequência de números inteiros.

Formato de entrada

Um inteiro

Formato de saída

Um inteiro"""


def brincando_fibonacci (n):

    if n < 4:
        return 1
    
    return brincando_fibonacci(n-1) + brincando_fibonacci(n-2)



indice = int (input())

print (brincando_fibonacci(indice))