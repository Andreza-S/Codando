"""Descrição
Chandu tem fascínio por strings e as classificou em Good string e Bad string.

- Good string : Não possui letras consecutivas iguais.

- Bad string : Contém letras consecutivas iguais.

Dado uma string S converta ela para Good string.

Você só tem um tipo de operação: Se duas letras consecutivas são iguais, elimine uma delas.

Formato de entrada

A primeira linha contém um inteiro T, indica o número de casos de testes.

Cada caso de teste terá uma linha com uma string S.

A string só possui letras minúsculas.

Formato de saída

Cada caso de teste imprima uma linha com Good string da palavra."""


def VerificarString (strings):

    for u in range (len(strings)):
        palvra_final = []

        for j in range (len(strings[u])):

            tamanho_palavra = (len(strings[u])) -1

            segundo_indice = j +1

            if j < (tamanho_palavra):        
                if (strings[u][j] != strings[u][segundo_indice]):
                    palvra_final.append(strings[u][j])
                else:
                    pass
            else:
                palvra_final.append(strings[u][j])
        
        palvra_final = "".join(palvra_final)
        print (palvra_final)

qtd_strings = int (input())

strings = []

for i in range (qtd_strings):
    letra_analisa = ""    
    string = input()
    strings.append(string)

VerificarString(strings)