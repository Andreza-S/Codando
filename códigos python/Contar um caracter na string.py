"""Descrição
Faça um programa para ler uma string e um caracter qualquer e calcule o número de ocorrências desse caracter na string. Exemplo: Seja a string "maracatu" e o caracter 'a', então o número de ocorrências é 3.

Formato de entrada

Você lerá duas linhas. Na primeira linha você receberá uma string com no máximo 50 caracteres. Na segunda linha você receberá um único caracter.

Formato de saída

Imprima um número inteiro indicando quantas vezes o caracter dado aparece na string.  Depois de imprimir o número, imprima um final de linha (ou seja, pule uma linha)."""


string = input()
analisar_caracter = input()

repeticoes_do_caracter = 0

for i in range (len(string)):
    if (string[i] == analisar_caracter):
        repeticoes_do_caracter += 1


print (repeticoes_do_caracter)