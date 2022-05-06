"""Descrição
Os funcionários do sindicato sempre se confraternizam no final do ano e o problema sempre está relacionado a como será a divisão da conta. Isto é, qual o modo mais justo a ser pago por cada sindicalista dado que há pessoas que ganham mais do que outras.

Uma sugestão enviada para a comissão organizadora foi:  cada um daria um valor igual ou inferior ao total sem ver quanto os demais dariam. Ao final, se calcularia a média e quem deu o maior valor de todos receberia o excedente. Dessa forma, cada um seria estimulado a dar o máximo que pudesse. A sugestão foi aceita!

Sendo assim, a sua função é construir um programa para simular a divisão da conta. O programa deve receber o valor total da conta, o número de sindicalistas que participarão da confraternização, o nome e o valor pago de cada um dos sindicalistas. Ao final, deve ser exibida uma mensagem indicando quem pagou mais e quanto e quanto recebeu. 

Formato de entrada

Um valor representando o valor total da conta a ser paga (ponto flutuante). Esse valor deve ser maior que zero.
Um valor inteiro indicando o número de sindicalistas (interior N), que deve ser maior que zero.
N strings correspondentes aos nomes de cada sindicalista
N valores correspondentes ao valor pago pord cada um dos N sindicalistas 
Formato de saída

Nome de quem pagou mais e quanto
Valor do excedente 
Duas situações são possíveis:

O valor arrecadado foi maior do que o valor da conta. Nesse caso, o sindicalista que pagou mais receberá um "troco", que é o valor excedente.
O valor arrecadado foi menor do que o valor da conta. Nesse caso, o valor arrecadado foi insuficiente para pagar a conta.
Observação: verifique os formatos possíveis de saída."""



valor_conta = float (input())
n_sind = int (input())

SIND_PAGOU_MAIS = ""
MAIOR_VALOR = 0


TOTAL_RECOLHIDO = 0
VALOR_EXCEDENTE = 0
VALOR_FALTA = 0 


if (valor_conta == 0 or n_sind == 0):
    print ("Nao ha conta ou funcionario suficiente para pagar a conta")
    exit()



for i in range (n_sind):

    nome_sind = input()
    sind_pagou = float (input())



    if (sind_pagou > MAIOR_VALOR):
        MAIOR_VALOR = sind_pagou
        SIND_PAGOU_MAIS = nome_sind
    
    else:
        pass

   
    TOTAL_RECOLHIDO += sind_pagou


if (MAIOR_VALOR == valor_conta):
    VALOR_EXCEDENTE = (TOTAL_RECOLHIDO - MAIOR_VALOR)
    print (SIND_PAGOU_MAIS + " pagou R$ {:.1f}".format (MAIOR_VALOR))
    print ("Valor excedente: sobra R$  {:.1f}".format (VALOR_EXCEDENTE))
    exit()


if (TOTAL_RECOLHIDO > valor_conta):
    VALOR_EXCEDENTE = (TOTAL_RECOLHIDO - valor_conta)
    print (SIND_PAGOU_MAIS + " pagou R$ {:.1f}".format (MAIOR_VALOR))
    print ("Valor excedente: sobra R$  {:.1f}".format (VALOR_EXCEDENTE))
    exit()

            
if (TOTAL_RECOLHIDO < valor_conta):
    VALOR_FALTA = (valor_conta - TOTAL_RECOLHIDO)

    print (SIND_PAGOU_MAIS + " pagou R$ {:.1f}".format (MAIOR_VALOR))
    print ("Valor insuficiente: falta R$  {:.1f}".format (VALOR_FALTA))
    exit()
