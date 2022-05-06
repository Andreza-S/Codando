"""Descrição
Nós vamos definir o superdígito de um inteiro x conforme as seguintes regras:

Se x possui apenas 1 dígito, então o superdígito é x.
Caso contrário, o super dígito de x é igual ao superdígito da soma dos dígitos de x.
Por exemplo, o superdígito de 9875 é calculado como:

superdígito (9875)
= superdígito (9+8+7+5)
= superdígito (29)
= superdígito (2+9)
= superdígito (11)
= superdígito (1 + 1)
= superdígito (2)
= 2

Sua missão é calcular o superdígito de um número x.
Você receberá dois números: n e k.
x é construído fazendo k concatenações de n.
Por exemplo,
se n = 123 e k = 4
então:
x = 123123123123


Formato de entrada

A entrada consiste de dois inteiros n e k separados por espaço.

Considere:

1 <= n <= 10^100000
1 <= k <= 10^5
Formato de saída

Uma única linha contendo o superdígito de x."""


def calcula_superdigito (x):

    if (len(x) > 1):
        soma = 0

        for i in range (len(x)):
            n = int (x[i])
            soma += n
        
        soma = str (soma)
        return (calcula_superdigito(soma))
    
    else:
        return (print(x))


n, k = input().split()

string = n
concatenacoes = int (k)

superdigitos = string*concatenacoes

calcula_superdigito(superdigitos)