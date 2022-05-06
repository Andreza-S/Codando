"""Descrição
Dado um texto inverta as palavras que estejam num local par no texto.

Formato de entrada

Um texto.

Formato de saída

O texto com as mudanças pedidas."""

texto = input().split()
texto_final = []

repeticoes = len(texto)

for i in range (repeticoes):
    if (i != 0) and ((i % 2) != 0):
        palavra = texto[i]
        palavra_invertida = []
        contagem_de_indice_invertida = -1  

        for k in range (len(palavra)):
        
            palavra_invertida.append(palavra[contagem_de_indice_invertida])
            contagem_de_indice_invertida += -1
        palavra_invertida = "".join(palavra_invertida)
        texto_final.append(palavra_invertida)
    else:
        texto_final.append(texto[i])


        

print (" ".join(texto_final))