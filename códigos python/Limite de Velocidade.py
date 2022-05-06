"""Descrição
Devido ao grande número de acidentes ocorridos recentemente na rua principal da cidade, um sistema de radares será instalado para multar os condutores que excederem os 50 km/h permitidos. Aqueles que excederem a velocidade, mas estiverem no máximo 10% acima da velocidade limite serão multados em R$ 230. Já os condutores que excederem a velocidade permitida em até 20% serão multados em R$ 340. Caso a velocidade do motorista exceda o limite em mais de 20%, ele terá que pagar uma multa de R$ 19,28 por cada km excedido.

Escreva uma função chamada CalculaMulta que receba como entrada a velocidade de um condutor e retorne o valor da multa que ele terá que pagar.

Formato de entrada

Um valor inteiro

Formato de saída

Um valor real"""


def CalculaMulta (velocidade_para_analise):

    velocidade_maxima = 50
    porcentagem_dez = ((velocidade_para_analise * 0.10) + velocidade_maxima)
    multa_de_dez = 230
    porcentagem_vinte = ((velocidade_para_analise * 0.20) + velocidade_maxima)
    multa_de_vinte = 340
    multa_excedente_de_vinte = 19.28
    
    multa = 0
    

    if (velocidade_para_analise  > velocidade_maxima and velocidade_para_analise <= porcentagem_dez):
        multa = multa_de_dez
    
    if (velocidade_para_analise  > porcentagem_dez and velocidade_para_analise <= porcentagem_vinte):
        multa = multa_de_vinte
    
    if (velocidade_para_analise > porcentagem_vinte):
        excedente = velocidade_para_analise - velocidade_maxima

        for i in range (excedente):
            multa += multa_excedente_de_vinte
    
    print ("{:.2f}".format (multa))


velocidade_do_condutor = int (input())

CalculaMulta (velocidade_do_condutor)