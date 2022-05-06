"""Descrição
A televisão por assinatura, até o mês de agosto do ano de 2011, possuía 11,6 milhões de clientes em todo o país. O setor era praticamente monopolizado por duas empresas, no entanto, outras empresas começaram a atuar e acirrar a concorrência. 

Para aumentar os clientes e, também incentivar os clientes a pagarem com débito automático, a empresa TáComTudo resolveu oferecer descontos e canais extras àqueles que aderirem nesta forma de pagamento. Clientes que escolherem pacotes Básico e Entretenimento ganham 5% de desconto e mais 6 canais, e para os demais pacotes ganham 10% de desconto e mais 11 canais.

Escreva um programa que receba como entrada o código do pacote e a forma de pagamento escolhida por um cliente, de acordo com a tabela abaixo, e exiba o valor final da mensalidade e a quantidade total de canais à qual ele terá direito.

Básico(código 1)- 32 canais e custa R$ 80.80

Entretenimento(código2)- 55 canais e custa R$ 100.40

Multicultural(código3)- 70 canais e custa R$ 130.23

Completo(código4)- 112 canais e custa R$ 215.50

As opções de pagamento podem ser: 

d ou D para Débito Automático 

c ou C para Cartão de crédito

a ou A para À vista 

Formato de entrada

um inteiro relativo ao código do pacote a ser contratado. No caso de ser informado um pacote inexistente, deve ser apresentada a mensagem: “Pacote selecionado invalido.”.

um caracter relativo à forma de pagamento. No caso de ser informado uma forma de pagamento inexistente, deve ser apresentada a mensagem: “Esta forma de pagamento não é possível”.

Formato de saída

Um valor real com duas casas decimais (valor final da mensalidade) e um inteiro (a quantidade total de canais à qual ele terá direito), da seguinte forma:

Valor contratado= R$ 80.80

Quantidade de canais= 32"""


Codigo_Pct = int (input())
Forma_Pg = input()


if (Codigo_Pct != 1) and (Codigo_Pct != 2) and (Codigo_Pct != 3) and (Codigo_Pct != 4):
    print ("Pacote selecionado invalido.")
    exit()

if (Forma_Pg != "a") and (Forma_Pg != "A") and (Forma_Pg != "b") and (Forma_Pg != "B") and  (Forma_Pg != "c") and (Forma_Pg != "C")  and  (Forma_Pg != "d") and (Forma_Pg != "D"):
    print ("Forma de pagamento invalida.")
    exit()


if (Forma_Pg == "d" or Forma_Pg == "D"): #Debito
   
    if (Codigo_Pct == 1):
        Valor_pctB1 = 80.80
        Qtd_CanaisB1 = 32

        Desconto = (Valor_pctB1 * (5/100))
        Valor_Final = (Valor_pctB1 - Desconto)
        Canais_Total = (Qtd_CanaisB1 + 6)
        print ("Valor contratado= R$ {:.2f}".format (Valor_Final))
        print ("Quantidade de canais= {}".format (Canais_Total))
    
    if(Codigo_Pct == 2):
        Valor_pctE2 = 100.40
        Qtd_CanaisE2 = 55

        Desconto = (Valor_pctE2 * (5/100))
        Valor_Final = (Valor_pctE2 - Desconto)
        Canais_Total = (Qtd_CanaisE2 + 6)
        print ("Valor contratado= R$ {:.2f}".format (Valor_Final))
        print ("Quantidade de canais= {}".format (Canais_Total))
        exit()

    if(Codigo_Pct == 3):
        Valor_pctM3 = 130.23
        Qtd_CanaisM3 = 70 
        
        Desconto = (Valor_pctM3 * (10/100))
        Valor_Final = (Valor_pctM3 - Desconto)
        Canais_Total = (Qtd_CanaisM3 + 11)
        print ("Valor contratado= R$ {:.2f}".format (Valor_Final))
        print ("Quantidade de canais= {}".format (Canais_Total))
    
    if(Codigo_Pct == 4):
        Valor_pctC4 = 215.50
        Qtd_CanaisC4 = 112

        Desconto = (Valor_pctC4 * (10/100))
        Valor_Final = (Valor_pctC4 - Desconto)
        Canais_Total = (Qtd_CanaisC4 + 11)
        print ("Valor contratado= R$ {:.2f}".format (Valor_Final))
        print ("Quantidade de canais= {}".format (Canais_Total))
        exit()


if (Forma_Pg == "c" or Forma_Pg == "C"): #Credito
    if (Codigo_Pct == 1):
        Valor_pctB1 = 80.80
        Qtd_CanaisB1 = 32
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctB1))
        print ("Quantidade de canais= {}".format (Qtd_CanaisB1))

    if (Codigo_Pct == 2):
        Valor_pctE2 = 100.40
        Qtd_CanaisE2 = 55
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctE2))
        print ("Quantidade de canais= {}".format (Qtd_CanaisE2))

    if (Codigo_Pct == 3):
        Valor_pctM3 = 130.23
        Qtd_CanaisM3 = 70
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctM3))
        print ("Quantidade de canais= {}".format (Qtd_CanaisM3))

    if (Codigo_Pct == 4):
        Valor_pctC4 = 215.50
        Qtd_CanaisC4 = 112
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctC4))
        print ("Quantidade de canais= {}".format (Qtd_CanaisC4))
        exit()


if (Forma_Pg == "a" or Forma_Pg == "A"): #A vista
    if (Codigo_Pct == 1):
        Valor_pctB1 = 80.80
        Qtd_CanaisB1 = 32
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctB1))
        print ("Quantidade de canais= {}".format (Qtd_CanaisB1))

    if (Codigo_Pct == 2):
        Valor_pctE2 = 100.40
        Qtd_CanaisE2 = 55
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctE2))
        print ("Quantidade de canais= {}".format (Qtd_CanaisE2))

    if (Codigo_Pct == 3):
        Valor_pctM3 = 130.23
        Qtd_CanaisM3 = 70
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctM3))
        print ("Quantidade de canais= {}".format (Qtd_CanaisM3))

    if (Codigo_Pct == 4):
        Valor_pctC4 = 215.50
        Qtd_CanaisC4 = 112
        print ("Valor contratado= R$ {:.2f}".format (Valor_pctC4))
        print ("Quantidade de canais= {}".format (Qtd_CanaisC4))