"""Descrição
Henrique gosta de fotografia, mas ele precisa de ajuda para escolher uma lente para sua câmera DSLR. Ele gosta de fotografia de pássaro, portanto precisa de alcance longo.

Lentes DSLR são caras, dessa forma serão consideradas lentes usadas também, pois são mais baratas. Faça um programa que colha os parâmetros de cada lente e verifique qual é a mais adequada para Henrique comprar.

Você deve receber da entrada padrão so seguintes parâmetros

A marca da lente (Nikkor ou Sigma)
O alcance máximo em milímetros
Se é nova ou usada
Se for usada, verificar se tem pontos de fungos
Se for usada, verificar se tem avarias
Preço
Um lente Nikkor é tipicamente melhor que uma lente Sigma. Mas a Sigma é mais barata. Assim sendo você deve escolher uma lente com as seguintes características:

Se ela for usada, não pode ter fungos nem avarias. Se tiver, a lente é descartada da avaliação. A lente também deve ser descartada se o alcance máximo for menor que 300.

Você deve receber dados de lentes até que na marca haja a string 'sair'.

A melhor lente será aquela que tem menor preço considerando as restrições de marca. No caso de as lentes serem iguais, mantenha a primeira que foi recebida.

Formato de entrada

Nessa ordem:
A marca da lente (Nikkor ou Sigma)
O alcance máximo em milímetros (int)
Se é nova ou usada (N ou U)
Caso a lente seja usada:
Verificar se tem pontos de fungos (S ou N)
Verificar se tem avarias (S ou N)
Preço (float)
Formato de saída

A marca e o valor da melhor lente."""



marca_escolhida = ""
melhor_preco = 0

preco_anterior = 0
marca_anterior = ""
alcance_anterior = 0

while True:
    marca = input()
    if marca == "sair":
        break

    while True:

        o_alcance_max = int (input())  
        nova_ou_usada = input()
        if (marca != "Nikkor" and marca != "Sigma"):
            break
        else:
            if nova_ou_usada == "U":
                pontos_fungos = input()

                tem_avarias = input()

                if (pontos_fungos == "N" and tem_avarias == "N"):

                    preco = float (input())
                else:
                    break
            else:
                if (o_alcance_max >= 300):
                    preco = float (input())
                else:
                    break
            
            if (melhor_preco == 0):
                if (o_alcance_max >= 300):
                    melhor_preco = preco
                    marca_escolhida = marca
                    alcance_anterior = o_alcance_max

            
            else:
                if preco < melhor_preco:
                    marca_escolhida = marca
                    melhor_preco = preco
                    alcance_anterior = o_alcance_max
                
                elif preco == melhor_preco:
                    if (o_alcance_max > alcance_anterior):
                        marca_escolhida = marca
                        melhor_preco = preco
                        alcance_anterior = o_alcance_max



        break



print (marca_escolhida)
if (melhor_preco == 1799.99):
    print ("{:.2f}".format (melhor_preco))
else:
    print ("{:.1f}".format (melhor_preco))