"""Descrição
Crie um programa que receba como entrada o valor total de uma dívida (número natural maior que zero) e o valor máximo que o devedor pode pagar todo mês (número natural maior que zero). O programa deve exibir o restante da dívida antes e depois de cada pagamento mensal até que a dívida zere. Obs.: quando a dívida é menor do que o máximo que o devedor pode pagar, ele pagará exatamente quanto deve, jamais pagará um valor superior.

Formato de entrada

Na primeira linha um valor natural maior que zero indicando o valor da dívida; na segunda linha o valor máximo que o devedor pode pagar por mês (novamente um valor natural maior que zero).

Formato de saída

O valor da dívida restante antes do pagamento mensal e o valor da dívida restante após o pagamento mensal, conforme o formato nos exemplos. Repetir enquanto a dívida não zerar."""


Divida = int (input())
V_pg = int (input())


while True:
    if (Divida > V_pg):
        print ("(antes) {}".format (Divida))
        depois_pg = (Divida - V_pg)
        print ("(depois) {}".format (depois_pg))
        Divida = (Divida - V_pg)
        
    if (Divida <= V_pg):
        print ("(antes) {}".format (Divida))
        print ("(depois) {}".format (Divida - Divida))
        break  