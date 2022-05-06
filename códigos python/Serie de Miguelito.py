"""Descrição
Miguelito gosta muito de séries numéricas e resolveu criar uma com seu nome. O primeiro valor da série de Miguelito é 3, e cada novo número é gerado somando-se ora 4 ora 1 ao valor anterior, de acordo com o exemplo abaixo:

3  7  8  12  13  17  18  22  23  27 ...

Escreva uma função recursiva chamada SerieMiguelito que receba como entrada o índice do elemento na sequência e retorne seu valor.

Formato de entrada

Um valor inteiro

Formato de saída

Um valor inteiro"""


def Serie_de_Miguelito (indice):

    lista_serie_Miguelito = [3]
    SOMA_1 = 1
    SOMA_4 = 4
    
    for i in range (indice-1):
        termo_MIguelito = lista_serie_Miguelito[i]

        if i % 2 != 0:
            lista_serie_Miguelito.append(termo_MIguelito+SOMA_1)
        else:
            lista_serie_Miguelito.append(termo_MIguelito+SOMA_4)
    
    return (print(lista_serie_Miguelito[indice-1]))


indice = int (input())

Serie_de_Miguelito(indice)