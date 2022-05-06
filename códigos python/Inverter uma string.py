"""Descrição
Leia uma string e inverta o seu conteúdo. Exemplo: Se a string digitada for "JANELA", então você deve imprimir: "ALENAJ".

Formato de entrada

Você receberá uma única linha contendo uma string com no máximo 255 caracteres.

Formato de saída

Imprima a string recebida com os seus caracteres invertidos também em uma única linha, seguida de um final de linha."""


string = input()

string_invertida = []
posicao = -1

for i in range (len(string)):
    string_invertida.append(string[posicao])
    posicao += -1

string_invertida = "".join(string_invertida)

print (string_invertida)