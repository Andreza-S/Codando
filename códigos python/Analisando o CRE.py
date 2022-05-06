"""Descrição
Fernanda tem um projeto de extensão e precisa selecionar alunos. Escreva um programa para que ela possa informar matrícula e CRE dos vários inscritos, e ver, ao final, a matrícula do aluno com menor CRE e o CRE médio de todos os candidatos.

Formato de entrada

Um String (matrícula) e um float (CRE) para cada candidato.

A entrada de dados deve parar quando for informada a matrícula 999

Formato de saída

Um String com a matrícula que teve o menor CRE, seguida por um float com duas casas decimais para a média de CREs.

Esses valroes devem ser separados por uma quebra de linha (enter)"""


mat_aluno_menor_cre = 0
menor_cre = 11
soma_cre = 0
qtde_cre = 0

while True:
    mat = int(input())
    if mat == 999:
        break
    cre = float (input())
    soma_cre += cre
    qtde_cre += 1
    if cre < menor_cre:
        menor_cre = cre
        mat_aluno_menor_cre = mat

print (mat_aluno_menor_cre)
print("{:.2f}". format (soma_cre/qtde_cre))