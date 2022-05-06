"""Descrição
As inscrições para o processo seletivo interno de monitores para todas as disciplinas do Centro Integrado de Passa-e-Fica estão abertas. A monitoria tem como objetivo promover a interação acadêmica entre discentes e docentes; estimular o(a) monitor(a) no desempenho de suas potencialidades e,subsidiar o o corpo discentedos diversoscursos na superação de dificuldades de aprendizagem e produção de novos conhecimentos nas disciplinas objeto da monitoria.

Os requisitos necessários são:

Ser aluno(a) regularmente matriculado(a);

Ter sido aprovado(a) e obtido média igual ou superior a 70(setenta) na disciplina objeto da inscrição;

Dispor de pelo menos 8 horas semanais exclusivamente no turno do curso/disciplina alvo da monitoria, para serem destinadas ao desenvolvimento do trabalho e para participar de reuniões com o professor orientador. 

A procura pela seleção de monitoria é alta. Por isso, faz-se necessário que você desenvolva um programa para indicar se o aluno foi ou não aprovado no processo de monitoria. O programa deve ler informação de vários candidatos até que a média informada seja igual a zero.

O aluno é aprovado para a monitoria quando atende a todos os requisitos e sua nota na prova de monitoria é igual ou superior a 70.

Formato de entrada

O aluno só poderá fazer a prova de monitoria se ele atender inicialmente ao requisito 1 e, depois ao requisito 2. 

A solução deve supor que os alunos inscritos estão todos regularmente matriculados. Dessa forma, deve-se ler inicialmente a média na disciplina que deseja concorrer (número inteiro, entre 0 e 100) e em seguida o nome do candidato.

Caso atenda ao requisito número 1, ler o tempo disponível (número inteiro). Os dados a seguir devem ser lidos quando o aluno atende aos requisitos estabelecidos:

CRE (número inteiro, entre 0 e 100)

nota da prova (número inteiro, entre 0 e 100)

Se o usuário digitar a média da disciplina fora do intervalo informado, deve apresentar uma mensagem (“Nota fora do intervalo”) e ler novamente a média até que seja informada uma média válida. O mesmo vale para a nota da prova.

Formato de saída

Uma mensagem e a nota final do aluno (com duas casas decimais) se o mesmo passou na monitoria.

A média final do aluno é uma média ponderada onde a média da disciplina vale 40%, o CRE vale 10% e a nota da prova vale 50%. Para um aluno ser aprovado, primeiro ele tem que ter nota da prova de monitoria igual ou superior a 70 e média final igual ou superior a 70.

Mensagens possíveis:

“Aluno “NAO pode concorrer.” - quando o aluno não passou na disciplina que deseja concorrer ou não tem o tempo mínimo exigido de horas semanais;
 "Aluno reprovado na prova de monitoria!“, quando o aluno não passou na prova de monitoria;
“Aluno aprovado! Sua media foi xx.xx.", quando o aluno passou na seleção de monitoria;
“Aluno reprovado na selecao. Media= xx.xx.”, quando o aluno não passou na seleção de monitoria.

A última mensagem exibida é o nome do candidato com maior nota e sua respectiva nota final. Exemplo: “Resultado da monitoria: nononno, xx.xx”. Caso não exista nenhum candidato aprovado, exiba a mensagem: “Resultado da monitoria: Sem alunos aprovados.”"""


MEDIA_DISCIPLINA_ACEITA = 70 #MAIOR OU IGUAL
HORAS_MINIMA = 8 #DISPOR DE PELO MENOS
NOTA_MINIMA_PROVA = 70 #NOTA MINIMA ACEITA PARA PROVA 
ENCERRAR = 0
MEDIA_MINIMA_MONITORIA = 70

media_aluno_monitoria = 0
quantidade_de_alunos_aprovados = 0

aluno_aprovado = ""
maior_media_monitoria = 0


while True:
    media_aluno_disciplina = int (input())
    if (media_aluno_disciplina == ENCERRAR):
        if (quantidade_de_alunos_aprovados > 0):
            print ("Resultado da monitoria: " +  (aluno_aprovado) + ", {:.2f}.".format (maior_media_monitoria))
        else:
            print ("Resultado da monitoria: Sem alunos aprovados.")
        exit ()

    while (media_aluno_disciplina < 0) or ((media_aluno_disciplina > 100)):
        # print ("Nota fora do intervalo")
        media_aluno_disciplina = int (input())
    
    else:
        nome = input()
        horas_disponiveis = int (input())

        if (media_aluno_disciplina < MEDIA_DISCIPLINA_ACEITA) or (horas_disponiveis < HORAS_MINIMA):
            print ("Aluno NAO pode concorrer.")
            pass      
        else:
            cre = int (input())
            nota_prova = int (input())
        
            while (nota_prova < 0) or ((nota_prova > 100)):
                # print ("Nota fora do intervalo")
                nota_prova = int (input())
        
            calculo_media_monitoria = ((40/100) * media_aluno_disciplina) + ((10/100) * cre) + ((50/100) * nota_prova)
            media_aluno_monitoria = calculo_media_monitoria
            
            if (media_aluno_monitoria > maior_media_monitoria):
                maior_media_monitoria = media_aluno_monitoria
                aluno_aprovado = nome
            else:
                pass

            if (nota_prova  < NOTA_MINIMA_PROVA):
                print ("Aluno reprovado na prova de monitoria!")
            
            else:
                if (media_aluno_monitoria  >= MEDIA_MINIMA_MONITORIA):
                    print ("Aluno aprovado! Sua media foi {:.2f}.".format (media_aluno_monitoria))
                    quantidade_de_alunos_aprovados += 1
                if (media_aluno_monitoria < MEDIA_MINIMA_MONITORIA):
                    print ("Aluno reprovado na selecao. Media= {:.2f}.".format (media_aluno_monitoria))