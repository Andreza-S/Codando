"""Descrição
Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números devem ser impressas a tabuada. Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5. O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam esses, emita uma mensagem de erro.



Formato de entrada

Dois números em 2 linhas distintas indicando o intervalos dos números das tabuadas.

Formato de saída

As tabuadas dos números dentro do intervalo."""


while True:
    inicio = int (input())
    if 1 <= inicio <= 9:
        break
    else:
        print ("Insira um numero inicial entre 1 e 9")

while True:
    fim = int (input())
    if 1 <= fim <= 9:
        break
    else:
        print ("Insira um numero final entre 1 e 9")

if fim >= inicio:
    for i in range (inicio, fim+1):
        for j in range(1, 10):
            print ("{} x {} = {}".format (i, j, i*j))
        print()
else:
    print("Nenhuma tabuada nesse intervalo")