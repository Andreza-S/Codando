"""Descrição
Você deve ajudar seu professor a descobrir qual a situação dos alunos de uma turma. Faça um programa que recebe como entrada 3 notas do usuário, calcula a média do aluno naquele semestre e, em seguida, informa a situação do aluno:

"Aprovado", se a média estiver no intervalo [70; 100]
"Reprovado", se a média estiver no intervalo [0; 40] 
"Final", se a média estiver no intervalo (40; 70).
"Média inválida" em qualquer outro caso.
Formato de entrada

Três notas (inteiros) em sequência com os valores de 0 a 100.

Formato de saída

Uma frase que informa a situação do aluno na disciplina e sua média no seguinte formato (sem acentos):

"A media do aluno foi 70.0 e ele foi APROVADO" (A saída deve ter aproximação de 2 casas decimais)

Nas seguinte condições:

"Aprovado", se a média estiver no intervalo [70; 100]
"Reprovado", se a média estiver no intervalo [0; 40] 
"Final", se a média estiver no intervalo (40; 70).
ou

"Media invalida" se as notas não compuserem uma média válida."""



N1 = int (input())
N2 = int (input())
N3 = int (input())

MediaF = ( (N1 + N2 + N3) / 3 )
if ( MediaF >= 70) and (MediaF <=100):
    print ("A media do aluno foi " + "{:.2f}".format (MediaF) + " e ele foi APROVADO")
elif ( MediaF <= 40 and MediaF > 0):
    print ("A media do aluno foi " + "{:.2f}".format (MediaF) +  " e ele foi REPROVADO")
elif ( MediaF > 40) and ( MediaF < 70):
    print ("A media do aluno foi " + "{:.2f}".format (MediaF) +  " e ele foi FINAL")
elif (MediaF < 0 or MediaF > 100 ):
    print ("Media invalida")