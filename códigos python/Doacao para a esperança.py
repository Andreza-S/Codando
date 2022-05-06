"""Descrição
No país onde tudo acontece também existe solidariedade. A solidariedade pode ser exercida por todos, os que participam e os que não participam, do programa que é a esperança às crianças e jovens do país. O objetivo é investir em projetos sociais a fim de beneficiar mais de 4 milhões de crianças, adolescentes e jovens em todo o país.

Como um cidadão pode contribuir? Doando um pouco do que tem. É simples! Qualquer um pode doar; uma única vez ou mensalmente. E qualquer valor maior ou igual a 1 real.

Os valores mais comuns são: 10, 20, 40 e 80. Mas pode ser qualquer um outro valor (>=1). Tem que escolher se será uma única vez ou mensal. Se mensal, é preciso informar por quantos meses será a doação.

A causa é nobre. Mas a organização está preocupada porque tem que informar periodicamente aos superiores quanto já foi doado e eles não conseguem fazer isso manualmente. 

Por isso a sua função é escrever um programa para ajudar os organizadores.

Formato de entrada

A entrada contém:

valor (int) da doação (valor deve ser maior ou igual a 1). Se for digitado um valor inferior a 1, o programa deve ser encerrado.

opção da doação: 1 (para 1 única vez) ou 2 (para doação mensal). Se forem digitados valores diferentes destes, deve ser apresentada uma mensagem de valor inválido.

Se a opção escolhida for 2, solicitar a quantidade de meses (m) em que haverá a doação (2 <= m <=12). Se forem digitados valores diferentes destes, deve ser apresentada uma mensagem informando os valores possíveis.

Formato de saída

Seu programa deverá apresentar o número total de doações realizadas para o momento atual (para o mês atual), com duas casas decimais,  e o valor previsto para os meses seguintes. Lembrando que, no caso de ser escolhida a opção de doação mensal, verificar o que será colocado em valor a receber num futuro próximo."""


qtd_meses = 0
total_agora = 0
total_futuro = 0


while True:
    valor = int (input())
    if (valor < 1):
        break
    else:
        total_agora += valor
        opcao_doacao = int (input()) 

        while (opcao_doacao != 1) and (opcao_doacao != 2):
            print ("Valor invalido")
            opcao_doacao = int (input())
        else:
            if (opcao_doacao == 1):
                qtd_meses = 1

            if (opcao_doacao == 2):
                meses = int (input())


                while (meses < 2) or (meses > 12):
                    print ("Favor digitar valor entre 2 e 12, inclusive")
                    meses = int (input())
                
                else:

                    qtd_meses = meses
                    calculo_futuro = ((meses-1) * valor)
                    total_futuro += calculo_futuro





print("Total arrecadado para agora: R$ {:.2f}".format (total_agora))
print("Total arrecadado para meses futuros: R$ {:.2f}".format (total_futuro))