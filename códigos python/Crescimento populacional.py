"""Descrição
Segundo o IBGE, a população de Ambrolândia em 2010 era de aproximadamente 5000 habitantes. O IBGE também verificou que nos anos seguintes houve um crescimento populacional constante de 2% a cada ano. Esse tipo de comportamento, na matemática, é chamado de Progressão Geométrica (PG). Isso significa que, dada uma série numérica, cada termo, a partir do segundo, é igual à multiplicação do termo anterior por uma constante q, chamada razão. No caso do crescimento populacional de Ambrolândia, considerando que a população de cada ano representa os termos de uma PG, a razão seria 1,02 e a população em 2016 seria igual a 5000 * 1,02. No entanto, por se tratar do número de habitantes, essa PG deve ser adaptada para que seus termos sejam sempre números inteiros.

Dada uma população inicial em um determinado ano, um percentual anual de crescimento populacional constante e um ano posterior qualquer, escreva uma função recursiva capaz de retornar uma lista contendo o número de habitantes dessa cidade do ano inicial ao ano final informados.
Formato de entrada

4 números inteiros, sendo eles: a população inicial da cidade (pi), o ano em que a cidade tinha essa população (ai), o percentual de crescimento populacional da cidade (q) e o ano até o qual pretende-se calcular o número de habitantes (af).

Formato de saída

A saída deverá apresentar o número de habitantes da cidade a cada ano, partindo do ano ai até o ano af."""


n_habitantes = int (input())
ano_inicio = int (input())
porcentagem =  int (input())
ano_final =  int (input())

RAZAO = ((porcentagem/100) + 1)

pos_calculo_habitantes = 0


lista_de_dados_ano = []
lista_de_dados_habitantes = []

for i in range (ano_inicio, ano_final+1):
    if (i == ano_inicio):
        lista_de_dados_ano.append (i)
        lista_de_dados_habitantes.append (n_habitantes)
        pos_calculo_habitantes = n_habitantes
    else:
        calculo_habitantes = (pos_calculo_habitantes * RAZAO)
        pos_calculo_habitantes = calculo_habitantes
        lista_de_dados_ano.append (i)
        lista_de_dados_habitantes.append (calculo_habitantes)

for j in range (len(lista_de_dados_ano)):
    print ("{} {:.0f}".format (lista_de_dados_ano[j], lista_de_dados_habitantes[j]))