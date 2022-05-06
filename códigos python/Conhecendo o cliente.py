"""Descrição
Uma loja deseja conhecer o perfil de seus (suas) clientes e para isso vai fazer uma pesquisa usando um programa que ficará no caixa. Ele vai perguntar a cada cliente no momento da compra  as seguintes informações: idade, valor da compra e tipo de pagamento (C: cartão; V: à vista). Essas perguntas serão feitas enquanto a resposta for (S)IM. Quando a resposta for (N)ÃO, a pesquisa deve ser encerrada e o programa deve exibir as seguintes informações:

A quantidade de vendas realizadas;
O total de vendas à vista e no cartão;
A idade do cliente mais jovem;
O valor da maior compra;
A média de compras feitas à vista;
Formato de entrada

Você deve receber do usuário as seguintes informações:

Idade (int)
Valor da compra (float)
Tipo de pagamento (C: cartão; V: à vista)
Um caractere "S" ou "N" que indica se o programa deve continuar ou não
Formato de saída

A saída é dada pelos seguintes valores (nessa ordem):
A quantidade de vendas realizadas (int);
O valor total de vendas à vista (float);
O valor total de vendas no cartão  (float);
A idade do cliente mais jovem (int); 
O valor da maior compra (float);
A média de compras feitas à vista (float);
Todos os valores float devem ter arredondamento de 2 casas decimais"""


qtd_vendas = 0

valor_total_aVista = 0

valor_total_Cartao = 0

idade_mais_jovem = 9999

maior_compra = 0

qtd_compras_aVISTA = 0

media_compras_aVISTA = 0


while True:
    idade = int (input())
    valor_compra = float (input())
    tipo_pag = input()

    qtd_vendas += 1

    if (tipo_pag == "V"):
        valor_total_aVista += valor_compra
        qtd_compras_aVISTA += 1
        calculo_media_avista = (valor_total_aVista/qtd_compras_aVISTA)
        media_compras_aVISTA = calculo_media_avista
    else:
        valor_total_Cartao += valor_compra

    if (idade < idade_mais_jovem):
            idade_mais_jovem = idade

    if (valor_compra > maior_compra):
        maior_compra = valor_compra

    continuar = input()
    if (continuar == "N"):
        break
    else:
        pass

print (qtd_vendas)

if (valor_total_aVista == 0):
    print ("{:.0f}".format (valor_total_aVista))
else:
    print ("{:.2f}".format (valor_total_aVista))

if (valor_total_Cartao == 0):
    print ("{:.0f}".format (valor_total_Cartao))
else:
    print ("{:.2f}".format (valor_total_Cartao))
    
print (idade_mais_jovem)

if (maior_compra == 0):
    print ("{:.0f}".format (maior_compra))
else:
    print ("{:.2f}".format (maior_compra))

if (media_compras_aVISTA == 0):
    print ("{:.0f}".format (media_compras_aVISTA))
else:
    print ("{:.2f}".format (media_compras_aVISTA))