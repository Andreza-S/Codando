"""Descrição
Marianna e Marinna são amigas e conversam bastante sobre muitos segredos. Para que as demais pessoas não lessem suas conversas criaram um código entre elas.
O código estabelece uma relação entre letras e números conforme mostrado abaixo.
Faça uma função chamada "traduzir", que recebe uma uma mensagem e retorna a mensagem traduzida. 


Formato de entrada

Como Marianna e Marianna conversam muito, a entrada consistirá de várias frases até que seja digitado "fim".

Cada linha consiste de uma sequência de números separados por um espaço em branco e deve ser traduzida, com exceção da linha que corresponder à palavra "fim".

Formato de saída

A mensagem traduzida."""


while True:
    lista_simbolos = [" ", "a", "b","c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n","o", "p", "q", "r" , "s", "t", "u", "v", "w", "x", "y", "z"]

    frase = input().split()
    frase = list(map(int, frase))
    fim = [6,9,13]
    if (frase == fim):
        exit()
    else:
        for i in range (len(frase)):

            indice_pesquisa = frase[i]
            
            print (lista_simbolos[indice_pesquisa], end = "")
        print()