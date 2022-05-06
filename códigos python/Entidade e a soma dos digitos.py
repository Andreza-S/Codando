"""Descrição
A Entidade foi desafiada pelos seus amigos à encontrar todos os números, entre 0 e N, cujas somas dos dígitos sejam exatamente igual a K. Ela se divertiu muito, mas ficou curiosa para saber quantos números mais podem ser encontrados e também quais são esses números. Ajude a Entidade a matar sua curiosidade.

Formato de entrada

A entrada consistirá de dois inteiros N e K, que representam, respectivamente, o maior número deve ser considerado na busca e a soma alvo.

Formato de saída

A saída deverá conter várias linhas, cada linha deverá conter um inteiro: o número cuja soma dos seus dígitos é exatamente K.
Em seguida, a saída deverá conter a quantidade de números que atendem à essa propriedade, veja o exemplo de saída para entender a formatação.

"""



import sys
sys.setrecursionlimit(10000)

def soma_digitos_lista (lista_digitos):

    soma = 0
    for t in range (len(lista_digitos)):
        soma += lista_digitos[t]

    return soma


def Soma_digitos (inicio, final, k, contador):

    if inicio == final:
        return print ("Numbers: {}".format (contador))

    n_str = str (inicio)
    digitos = []

    for i in range (len(n_str)):

        digito_int = int (n_str[i])
        digitos.append(digito_int)
            
    
    soma_final = soma_digitos_lista(digitos)

   
    if soma_final == k:
        contador +=1
        print (inicio)
                      
    Soma_digitos(inicio+1, final, k,contador)
        
n, k = input().split()

final = int (n)
k = int (k)
inicio = 0
contador = 0


Soma_digitos (inicio, final, k, contador)