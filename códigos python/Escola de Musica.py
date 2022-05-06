"""Descrição
A Escola de Música Melodia é bastante conceituada na cidade e forma grandes profissionais. Para isso, exige que seus alunos tenham no máximo 10 faltas por semestre, e que obtenham média mínima 7 para serem aprovados. Aqueles que não excedem o limite de faltas e conseguem média igual ou superior a 9,5 são aprovados com louvor.

Escreva uma função chamada ClassificaAluno que receba como entrada a media e a quantidade de faltas de um aluno e retorne sua situação ao final do semestre.

Formato de entrada

Um número real e um número inteiro, nessa ordem

Formato de saída

Um String em letras maiúsculas (APROVADO COM LOUVOR ou APROVADO ou REPROVADO ou REPROVADO POR FALTAS)"""


def ClassificaAluno (media, faltas):
    
    REPROVADO = "REPROVADO"
    APROVADO_COM_LOUVOR = "APROVADO COM LOUVOR"
    APROVADO = "APROVADO"
    REPROVADO_POR_FALTAS = "REPROVADO POR FALTAS"
    
    
    MEDIA_APROVADO_COM_LOUVOR = 9.5
    MEDIA_MINIMA = 7.00
    FALTAS_MAXIMA = 10

    if (media < MEDIA_MINIMA):
        print (REPROVADO)
    
    if (faltas > FALTAS_MAXIMA):
        print(REPROVADO_POR_FALTAS)

    if (media >= MEDIA_MINIMA and faltas <= FALTAS_MAXIMA):
        if (media >= MEDIA_APROVADO_COM_LOUVOR):
            print (APROVADO_COM_LOUVOR)
        else:
            print (APROVADO)

nota_media = float (input())
qtd_faltas = int (input())

ClassificaAluno(nota_media, qtd_faltas)