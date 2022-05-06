"""Descrição
Sabe-se que anos bissextos são os anos que possuem 366 dias no calendário, esse dia representa o acrescimo de 1 dia em Fevereiro, que deixa de ter 28 dias, e passa a ter 29.

 

Formato de entrada

Dois inteiros, representando um ano inicial, e um ano final.

Formato de saída

Todos os anos bissextos entre os dois anos dados, inclusive.

Se não houver anos bissextos, imprimir "-1", sem as aspas.

Obs: a saida deve ser seguida de uma quebra de linha."""


a1, a2 = input().split()

anoI = int (a1)
anoF = int (a2)

tem_anos_bissextos = False

for i in range (anoI, anoF+1):
    if (i % 4 ==0) and (i % 400 ==0 or i % 100 !=0):
            print (i)
              
            tem_anos_bissextos = True

if (tem_anos_bissextos == False):

    print (-1, end = " ") 
