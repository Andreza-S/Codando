'''
Projeto 5: Aplicação de Churrasco com Validação de CEP e CPF

Este projeto contem uma aplicação em Python simples que ajudará os usuários a
planejar um churrasco. A aplicação deve seguir as seguintes funções:

➔ Validação de CEP:
◆ Os usuários inserirão seu CEP para verificar a disponibilidade de entrega de
produtos para o churrasco.
◆ API de consulta de CEP para verificar se o CEP é válido e quais opções de entrega estão disponíveis.
➔ Validação de CPF:
◆ Os usuários fornecerão o CPF e o sistema deve verificar se é um número de
CPF válido.
Além disso existem funções para edição dos dados.
➔ Cálculo de Carne e Bebidas:
◆ Após a validação bem-sucedida do CEP e do CPF, os usuários poderão inserir
o número de convidados para o churrasco e a aplicação calculará
automaticamente a quantidade de carne e bebidas necessárias com base
em um conjunto de regras pré-definidas.
➔ Apresentação dos Resultados:
◆ A aplicação exibirá os resultados do cálculo, incluindo a quantidade de carne
e bebidas necessárias, além das opções de entrega disponíveis com base no
CEP. 
'''
import requests
from validate_docbr import CPF


def validar_cep(cep):
    ERRO = {'erro': True}

    # Construir a URL para consulta na API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    # Enviar uma solicitação HTTP GET para a API ViaCEP
    response = requests.get(url)

    # Se o CEP for válido:
    if response.status_code == 200:
        # Se a resposta da API for bem-sucedida (status 200), analisar os dados JSON
        data = response.json()
        # Tratando erro do retorno do CEP
        if data == ERRO:
            print ("CEP inválido\n")
            return (None)
        # Caso o CEP seja válido: retorno os dados da resposta, como data['logradouro'], data['bairro'], etc.
        else:
            print ("CEP Válido\n")
            return (data)
    # Se o CEP for inválido:
    # Se a resposta não for bem-sucedida, retornar None
    else:

        print ("CEP inválido\n")
        return (None)
        
#---------------------------FIM-------------------------------------------


def inserir_novo_cep ():
    cep = input ("Por favor insira um novo cep: ")
    return (validar_cep(cep)) # Retorna a validação do novo CEP

#-----------------------------FIM-----------------------------------------



def numero_end ():
    numero = input("Por favor insira o número do imóvel para entrega: ")
    return numero #retorna o numero do imóvel que receberá a entrega

#----------------------------FIM------------------------------------------


def complemento_end ():
    complemento = input ("\nPor favor insira o complemento do endereço (nome do condomínio/sitio; apartamento e ponto de referência): ")
    return (complemento) # Retorna as informações do complemento fornecidas
#-----------------------------FIM------------------------



def confirma_end (cep, numero, complemento):
    CONFIRMO = "1"
    EDITAR = "2"
    confirma = ""

    print ("\nPor favor confirme o endereço para entrega:")
    print (f"{cep['logradouro']}, {numero}, {cep['bairro']}, {cep['localidade']}, {cep['uf']}, {cep['cep']}.\n{complemento}\n")
    endereco_compl = (f"{cep['logradouro']}, {numero}, {cep['bairro']}, {cep['localidade']}, {cep['uf']}, {cep['cep']}.\n{complemento}\n")

    while (confirma != CONFIRMO and confirma != EDITAR):
        confirma = input("Digite 1 para confirmar ou 2 para editar os dados: ")
    
    if confirma == EDITAR:
        CEP = "1"
        NUMERO = "2"
        COMPLEMENTO = "3"
        opcao_editar = ""
        while (opcao_editar != CEP and opcao_editar != NUMERO and opcao_editar != COMPLEMENTO):
            opcao_editar = input ("\nEscolha o que você deseja editar:\n1 - CEP\n2 - Numero do imóvel\n3 - Complemento\nDigite sua opção: ")
        
        return opcao_editar
    else:
        print ("Endereço Confirmado\n")
        return endereco_compl
#-----------------------------------FIM----------------------------------------

def editar_cep():
    cep = inserir_novo_cep()
    return cep
#------------------------FIM-------------------------


def editar_numero():
    numero = numero_end()
    return numero
#------------------------FIM-------------------------


def editar_complemento():
    complemento = complemento_end()      
    return complemento
#------------------------FIM-------------------------
#-----------------------------------------------FIM DAS FUNÇÕES DE ENDEREÇO---------------------------------------


def validar_cpf(cpf):
    # Criar uma instância da classe CPF para validação
    cpf_validator = CPF()
    # Chamar o método validate para verificar se o CPF é válido
    if cpf_validator.validate(cpf) is True: #Se o CPF for válido
        print ("CPF Validado\n")
        return cpf
    else:
        print ("CPF Inválido\n")
        return None  #Se o CPF for inválido
    
#---------------------------FIM--------------------------------------------


def inserir_novo_cpf():
    cpf = input("Por favor insira um novo CPF: ")
    return (validar_cpf(cpf)) # Retorna a validação do CPF

#----------------------FIM-------------------------
#-----------------------------------------------FIM DAS FUNÇÕES DE CPF---------------------------------------



def inserir_convidados():
    convidados = input("Por favor insira a quantidade de pessoas que serão convidadas para o seu churrasco: ")
    return convidados
#--------------------------------------------FIM---------------------------


def calcular_carne_e_bebidas(convidados):
    # Definir as quantidades padrão por convidado
    CARNE_POR_CONVIDADO = 0.5  # Exemplo: 500g por pessoa
    BEBIDAS_POR_CONVIDADOS = 1  # Exemplo: 1 litro por pessoa

    # Calcular a quantidade total com base no número de convidados
    quantidade_carne = CARNE_POR_CONVIDADO * int(convidados)
    quantidade_bebidas = BEBIDAS_POR_CONVIDADOS *int(convidados)

    # Retornar as quantidades calculadas
    return (f"\nSão indicados {quantidade_carne} Kg de carne e {quantidade_bebidas} Litros de bebidas para {convidados} convidados do seu churrasco.\n(Foram calculados 500g de carne e 1 Litro de bebiba por convidado)\n")

#------------------------FIM----------------------------------------------------


def confirma_calculo_carne_bebidas():
    SIM = "1"
    EDITAR = "2"
    confirma = input("Você confirma essa a quantidade de convidados?\nEscolha a opção:\n1 - Sim\n2 - Editar quantidades de convidades\nDigite sua opção: ")
    while (confirma != SIM and confirma != EDITAR):
        print ("Por favor insira uma opção válida.")
        confirma = input("Você confirma essa a quantidade de convidados?\nEscolha a opção: 1 - Sim\n2 - Editar quantidades de convidades\nDigite sua opção: ")
    return confirma
#---------------------------------FIM-----------------------
#-------------------------------------FIM DAS FUNÇÕES DE CONVIDADOS , CARNE E BEBIDAS--------------------------------------





def agendar():
        CONFIRMO = "1"
        EDITAR = "2"
        confirma = ""

        while (confirma != CONFIRMO):
            data = ""
            horario = 0
            data = input ("\nPor favor digite o DIA/MÊS/ANO em que você dseseja que a entrega seja feita: ")
            horario = input ("\nAgora digite a HORA da entrega.\nOs horários disponíveis são em intervalos de uma em uma hora, por exemplo:\n08, 09, 10, 11, 12, 13, 14, 15, 16, 17 ou 18.\nDigite apenas numeros no formato de 24h (entregas são feitas a partir das 08h da manhã até às 18h da tarde): ")
            horario = int(horario)

            while (horario < 8 or horario > 18): 
                print ("Por favor digite um horário válido.")
                horario = input ("Agora digite a HORA da entrega.\nOs horários disponíveis são em intervalos de uma em uma hora, por exemplo:\n08, 09, 10, 11, 12, 13, 14, 15, 16, 17 ou 18.\nDigite apenas numeros no formato de 24h (entregas são feitas a partir das 08h da manhã até às 18h da tarde): ")
                horario = int(horario)
            
            confirma = input(f"Você confirma o agendamento para:\n{data} no horario das {horario}h ?\nEscolha a opção:\n1 - Confirmo\n2 - Editar data e horário\nDigite sua opção: ")

            while (confirma != CONFIRMO and confirma != EDITAR):
                confirma = input(f"Você confirma o agendamento para:\n{data} no horario das {horario}h ?\nOpções:\n1 - Confirmo)\n2 - Editar tipo de entrega\nDigite sua opção: ")

        return (f"\nA entrega será feita em {data} às {horario} h")
#-----------------------------FIM------------------------------


def tipo_de_entrega():
    AGORA = "1"
    AGENDAR = "2"
    ENTREGA_AGORA = ("Entrega será feita agora")

    def opcao():
        tipo_entrega = input ("Por favor agora selecione o tipo de entrega:\n1 - Entregar Agora\n2 - Agendar\nDigite sua opção: ")

        while (tipo_entrega != AGORA and tipo_entrega != AGENDAR):
            tipo_entrega = input("\nPor favor insira uma opção válida.\nPor favor agora selecione o tipo de entrega:\n1 - Entregar Agora\n2 - Agendar\nDigite sua opção: ")

        return tipo_entrega

    if opcao() == AGENDAR:
        data_horario_entrega = agendar()
    else:
        data_horario_entrega = ENTREGA_AGORA

    return data_horario_entrega

#----------------------------------FIM-----------------------------
#----------------------------------FIM DAS FUNÇÕES DE TIPO DE ENTREGA----------------------------




#--------------INICIO DO PROGRAMA---------------------------

# Recebendo CEP:
print("\n---------------------------------------------INICIO DO PROGRAMA--------------------------------------------------------------------\n")
print("\nDados do endereço para entrega\n")
cep = inserir_novo_cep()

while (cep == None):
    cep = inserir_novo_cep() # Se o CEP for inválido, repete-se a solicitação de um CEP

# Recbendo numero e  complemento de endereço
numero = numero_end()
complemento = complemento_end()

# Confirmando o endereço completo
confirma = confirma_end(cep, numero, complemento)
CEP = "1"
NUMERO = "2"
COMPLEMENTO = "3"

while (confirma == CEP or confirma == NUMERO or confirma == COMPLEMENTO):
    if confirma == CEP:
        cep = editar_cep()
        confirma = confirma_end(cep, numero, complemento)
    elif confirma == NUMERO:
        numero = editar_numero()
        confirma = confirma_end(cep, numero, complemento)
    else:
        complemento = complemento_end()
        confirma = confirma_end(cep, numero, complemento)

endereco_compl = (f"{cep['logradouro']}, {numero}, {cep['bairro']}, {cep['localidade']}, {cep['uf']}, {cep['cep']}.\n{complemento}\n")
print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nDados de identificação\n")

# Confirmando o CPF
cpf = inserir_novo_cpf()

while (cpf == None):
    cpf = inserir_novo_cpf()
print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nDados para calcular a quantidade de Carne (Kg) e bebibdas (Litros)\n")

# Receber quantidade de convidados para calcular Carne (kg) e Bebidas (litros)
CONFIRMO = "1"
confirma_calculo = ""

while (confirma_calculo != CONFIRMO):
    convidados = inserir_convidados()
    qtd_carne_bebidas = calcular_carne_e_bebidas(convidados)
    print (qtd_carne_bebidas)
    confirma_calculo = confirma_calculo_carne_bebidas()

print("\n-----------------------------------------------------------------------------------------------------------------\n")
print("\nDados para a entrega\n")

# Confirmando o tipo de entrega
data_horario_de_entrega = tipo_de_entrega()


print("\n-----------------------------------------------------------------------------------------------------------------\n")

# Resumo da compra
CONFIRMO = "1"
CANCELAR = "2"
confirma = ""

print ("Confirme os dados para entrega do seu churrasco:\n")
print (f"\n{qtd_carne_bebidas}{data_horario_de_entrega}.\n")
print (f"No seguinte endereço: {endereco_compl}\n")

while (confirma != CONFIRMO and confirma != CANCELAR):
    confirma = input("Você confirma a compra?\nEscolha entre as opções:\n1 - CONFIRMO\n2 - CANCELAR\nDigite sua opção): ")

if (confirma == CONFIRMO):
    print ("Agredecemos a confiança e desejamos um Bom Churrasco.\nAté a próxima!")
else:
    print ("Se desejar refazer o processo execute novamente.\nAté a próxima!")
    exit
    

print("\n---------------------------------------------FIM DO PROGRAMA--------------------------------------------------------------------\n")


        









