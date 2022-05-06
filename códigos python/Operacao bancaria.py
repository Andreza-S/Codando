"""Descrição
Escreva um programa para implementar uma aplicação que lê um conjunto de operações bancárias e depois executa as mesmas. O programa aceita até 100 operações de crédito e débito. 

O programa deve obrigatoriamente ser dividido em 3 partes que:

1 - Lê as operações de uma vez salvando-as em um array com duas dimensões (operação e valor);

2 - Varre o array executando as operações;

3 - Imprime um resumo com os totais de valores a) creditados, b) debitados, e c) o saldo final resultante.

Todas as operações são executadas em uma mesma conta bancária. O saldo inicial da conta é zero.

Formato de entrada

Uma sequência de até 100 linhas, cada uma contendo dois valores. O primeiro (do tipo int) indica as operações de crédito (1) ou débito (0), o segundo (do tipo double) representa o valor a ser utilizado na operação. O que define o final da lista de operações é uma linha adicional, contendo apenas o valor int -1. Esta linlha final não deve ser armazenada no array.

Embora seu programa possa apenas aceitar vírgula como separador de decimal, o thehuxley vai requerer ponto como separador, mas você não precisa modificar nada no seu programa, pois a conversão é automática e depende apenas das configurações regionais do computador.


Formato de saída

Um resumo das operações realizadas em três linhas:

a 1a linha indica o total de valores creditados;
a 2a linha indica total de valores debitados;
a 3a linha indica o saldo da conta.
Os valores devem conter dois dígitos após a vírgula."""




operacoes = []
valores = []



while True: #recebendo entradas e construindo listas de operacoes e valores

    entrada = input()
    if (entrada == "-1"):
        break
    
    else:
        entrada = entrada.split()

        for i in range (len(entrada)):
            if i == 0:
                operacoes.append(entrada[i])

            else:
                valores.append(entrada[i])

operacoes = list(map(int, operacoes)) #convertendo em inteiros
valores = list(map(float, valores)) #convertando em floats

creditos = 0
debitos = 0



for h in range (len(operacoes)): #soma dos valores em credito e debito
    if (operacoes[h] == 1):
        
        creditos += valores[h]
    else:

        debitos += valores[h]

saldo = (creditos - debitos) #subtracao entre creditos e debitos para obter o saldo final

print ("Creditos: R$ {:.2f}".format (creditos))
print ("Debitos: R$ {:.2f}".format (debitos))
print ("Saldo: R$ {:.2f}".format (saldo))
