"""Descrição
Um número natural é  triangular se ele é produto de três números naturais consecutivos. Por exemplo: 120 é triangular, pois 4*5*6 = 120. O número 2730 é triangular, pois 13*14*15 = 2730. Dado um número natural (inteiro não-negativo) n, verifique se ele é triangular ou não. 

Formato de entrada

Um número natural

Formato de saída

Caso o número seja triangular, apresentar quais números formam o número triangular e a mensagem Verdadeiro. Veja exemplo a seguir:

13*14*15 = 2730

Verdadeiro

Caso o número não seja triangular, apresente a mensagem Falso."""


n = int (input())

achei = False
sequencia = ""

for i in range (1, n):
    if i*(i+1)*(i+2) == n:
        sequencia = "{} * {} * {} = {}".format (i, i+1, i+2, n)
        achei = True

if achei:
    print (sequencia)
    print ("Verdadeiro")

else:
    print("Falso")