"""Descrição
Carla é uma profissional muito dedicada! Ela é responsável por analisar o pH de várias substâncias e determinar se elas são ácidas, básicas ou neutras. Ela não para enquanto não tiver terminado de analisar todas as soluções pendentes.

Escreva um programa para ajudar a nossa querida Carla no seu trabalho. O programa vai receber como entrada uma sequência de números, cada um em uma linha, representando o pH de cada solução. A última entrada vai ser o número -1, indicando que não há mais soluções para serem analisadas e o programa pode encerrar sua execução. 

Para cada solução, o programa vai determinar a sua acidez: ACIDA (pH menor que 7), BASICA (pH maior que 7), ou NEUTRA (pH igual a 7). 

E aí, você vai ajudar a Carla? Bom trabalho!

Formato de entrada

A entrada é composta por diferentes números, cada um em uma linha. O último número sempre será -1.0..

Formato de saída

A saída terá as palavras ACIDA, BASICA e/ou NEUTRA, escritas em maiúsculas e sem acentos.

Note que quando a entrada for o número -1, nada a mais deve ser impresso na tela"""


while True:
    pH = float (input())
    if (pH == -1):
        break
    if (pH > 0):
        if (pH > 0 ) and (pH < 7 ): # ACIDA (pH menor que 7),
            print ("ACIDA")
        if (pH > 7):
            print ("BASICA") # BASICA (pH maior que 7),
        if (pH == 7):
            print ("NEUTRA") # ou NEUTRA (pH igual a 7).