"""Descrição
Na álgebra linear, o traço de uma matriz quadrada é a função matricial que associa a matriz à soma dos elementos da sua diagonal principal.

(https://pt.wikipedia.org/wiki/Tra%C3%A7o_(%C3%A1lgebra_linear))

traço(A) = a11 + a22 + ... + ann

Dada uma matriz quadrada de ordem n, calcule o traço dessa matriz.

Formato de entrada

É dado um inteiro n que representa a ordem da matriz quadrada.

Em seguida é dada a matriz como no exemplo:

3
1 2 3
4 5 6
7 8 9

Formato de saída

Você deve imprimir os valores utilizados para o cálculo do traço e o próprio valor do traço segundo o modelo a seguir:

tr(A) = (1.00) + (5.00) + (9.00) = 15.00

Observe que os valores devem estar impressos dentro de parênteses e com 2 casas decimais. Observe também que entre os valores e os sinais matemáticos (por exemplo: o sinal da soma + e o sinal de =) existe um espaço. Após o valor do traço, incluir um final de linha."""


ordem_matriz_quadrada = int (input())

matriz = []


for i in range (ordem_matriz_quadrada):
    valor = input().split()
    valor = list(map(float,valor))
    matriz.append(valor)

valores_do_traco = []

for u in range (len(matriz)):
    for o in range (len(matriz[u])):
        if (u == o):
            valor_para_somar = matriz[u][o]
            valores_do_traco.append(valor_para_somar)

print ("tr(A) = ", end = "")

repeticoes_da_impressao = (len(valores_do_traco))
soma_dos_valores_do_traco = 0

for z in range(len(valores_do_traco)):

    valor_atual = (valores_do_traco[z])
    soma_dos_valores_do_traco += valor_atual

    if (z < (repeticoes_da_impressao -1)): 
        print ("({:.2f}) + ".format (valores_do_traco[z]), end = "")
    else:
        print ("({:.2f}) = {:.2f} ".format (valores_do_traco[z], soma_dos_valores_do_traco))