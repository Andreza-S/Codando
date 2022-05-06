"""Descrição
Um grupo grande de pessoas fez várias apostas na Mega Sena e precisa de um programa para ajudá-los a conferir se houve ganhadores. Você foi encarregado de fazer um programa que indica apenas quantos foram os apostadores que acertaram os 6 números.

Seu programa deve conter uma função que, dado uma aposta e os valores da Mega Sena, indicar se a aposta é ou não vencedora.

Formato de entrada

Na primeira linha é fornecido o resultado oficial, formado por 6 números inteiros separados por espaços. Nas linhas seguintes, são fornecidas as apostas. Cada aposta é formada por 6 a 10 números inteiros separados por vírgulas. A linha contendo a string 'FIM' indica o fim das apostas.


Formato de saída

A saída consiste da string “Total de ganhadores:” seguida por um espaço em branco e do número de apostas que contêm os números do resultado, ou seja, o número de ganhadores.



Entrada	Saída
5 6 7 8 9 10	Total de ganhadores: 2
3,4,5,6,7,8,9
1,2,3,4,5,6,7,8,9,10	
5,6,7,8,9,10	
4,7,8,9,10,11	
FIM


Entrada	Saída
2 6 8 10 14 15	Total de ganhadores: 1
10,20,30,40,50,55
1,3,5,7,9,11	
2,4,6,8,10,12,14,15	
FIM"""




total_ganhadores = 0
numeros_ganhadores =  input().split()

numeros_ganhadores = list(map(int, numeros_ganhadores))
numeros_ganhadores.sort()


while True:
    n_apostados = input()
    if n_apostados == "FIM":
        break
    else:
        n_apostados = n_apostados.replace(",", " ")
        inteiros_n_apostados = n_apostados.split(" ")
        inteiros_n_apostados = list(map(int, inteiros_n_apostados))
      
        inteiros_n_apostados.sort()

        acertados = []

        for i in range(len(inteiros_n_apostados)):
            for j in range (len(numeros_ganhadores)):
                if (inteiros_n_apostados[i] == numeros_ganhadores[j]):
                    acertados.append(inteiros_n_apostados[i])
        
        acertados.sort()
        if (acertados == numeros_ganhadores):
            total_ganhadores += 1

print ("Total de ganhadores: {}".format ((total_ganhadores)))