"""Descrição
Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores, o maior valor lido , o valor delta e a soma dos elementos da diagonal princial.


O delta é igual a 1 se o maior valor for positivo, -1 se for negativo e zero se for zero.

Formato de entrada

9 valores inteiros referentes aos elementos da matriz.

Formato de saída

4 valores numéricos: o primeiro é um número em ponto flutuante de duas casas decimais e os outros três inteiros."""



QTD_LINHAS = 3
QTD_COLUNAS = 3

DELTA_MAIORVALOR_POSITIVO = 1
DELTA_MAIORVALOR_NEGATIVO = -1
DELTA_MAIORVALOR_ZERO = 0


soma_dos_valores = 0
soma_diagonal_principal = 0

maior_valor = 0

matriz = []

for i in range (QTD_LINHAS): #criacao da matriz e soma dos valores para calculo de media e soma da diag. principal
    linha = []
    for j in range (QTD_COLUNAS):
        valor = int (input())
        if i == 0 and j == 0:
            maior_valor = valor
        else:
            if (valor > maior_valor):
                maior_valor = valor

        soma_dos_valores += valor
            
        if ( i == j): #calculo da soma da diag. principal
            soma_diagonal_principal += valor 
    
        linha.append (valor)

    matriz.append(linha) #adicionando os valores a matriz

media_dos_valores = (soma_dos_valores / (QTD_COLUNAS*QTD_LINHAS))

delta_final = 0

#analisando a condicao para impressao do delta
if (maior_valor > 0):
    delta_final = DELTA_MAIORVALOR_POSITIVO
if (maior_valor < 0):
    delta_final = DELTA_MAIORVALOR_NEGATIVO
if (maior_valor == 0):
    delta_final = DELTA_MAIORVALOR_ZERO

print ("{:.2f} {} {} {}".format (media_dos_valores, maior_valor, delta_final, soma_diagonal_principal))