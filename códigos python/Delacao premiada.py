"""Descrição
Você precisa ajudar um juiz a decidir se um réu pode fazer delação premiada.

O tempo de um juiz é caro e ele vai alocar um estagiário para preencher seu sistema com diversas informações que o ajudarão a decidir para cada caso se o réu tem direito aos benefícios da delação.

A delação só pode ser feita em casos que apresentam certas propriedades.

O crime que será delatado tem que ser de maior dano à sociedade do que o crime praticado pelo delator. Os crimes considerados (em ordem de gravidade) serão:
Roubo (menor gravidade)
Tráfico
Homicídio (maior gravidade)
Se o crime do delator for de roubo ou tráfico e o crime delatado for de homicídio, ele tem direito à delação diretamente
Se o crime do delator for de roubo e o crime delatado for também de roubo, ele só tem direito à delação se o valor do roubo delatado for mais de 5 vezes maior que o do roubo do delator
Se o crime do delator for de roubo e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga traficada for mais de 3 vezes maior que o do roubo do delator
Se o crime do delator for de tráfico e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga traficada for mais de 5 vezes maior que o do tráfico do delator
No caso do delator ter cometido um homicídio e quiser delatar um homicídio, a delação será concedida
Se a delação foi concedida, você deve imprimir a seguinte mensagem:
"Delação concedida."
Caso contrário:
"Delação rejeitada."
Casos de erro:
Se qualquer um dos crimes for diferente dos especificados (roubo, tráfico ou homicídio), você deve gerar a seguinte mensagem:
"Crime inválido."
Formato de entrada

Nessa ordem:

O crime do delator (roubo, tráfico ou homicídio)
O valor do crime do delator (apenas em caso de roubo ou tráfico)
O crime delatado (roubo, tráfico ou homicídio)
O valor do crime delatado (apenas em caso de roubo ou tráfico)
Obs.: Você só deve receber esses valores se o crime for roubo ou tráfico
Formato de saída

Se a delação foi concedida, você deve imprimir a seguinte mensagem:
"Delação concedida."
Caso contrário:
"Delação rejeitada."
Se qualquer um dos crimes for diferente dos especificados (roubo, tráfico ou homicídio), você deve gerar a seguinte mensagem:
"Crime inválido."""



delator = input ()

resultado = ""

if delator != "roubo" and delator != "trafico" and delator != "homicidio":
    print ("Crime invalido.")
    exit(0)

if delator == "roubo" or delator == "trafico":
    Valor_delator = int (input())

DelatadO = input()
if DelatadO != "roubo" and DelatadO != "trafico" and DelatadO != "homicidio":
    print ("Crime invalido.")
    exit(0)
    
if DelatadO == "roubo" or DelatadO == "trafico":
    valor_DelatadO = int(input())

if delator == "roubo" and DelatadO == "roubo":
    if valor_DelatadO > 5*Valor_delator:
        resultado = "Delacao concedida."
    else:
        resultado = "Delacao rejeitada."

if delator == "roubo" and DelatadO == "trafico":
    if valor_DelatadO > 3*Valor_delator:
        resultado = "Delacao concedida."
    else:
        resultado = "Delacao rejeitada."
    
if delator == "trafico" and DelatadO == "trafico":
    if valor_DelatadO > 5*Valor_delator:
        resultado = "Delacao concedida."
    else:
        resultado = "Delacao rejeitada."

if delator == "homicidio":
    if DelatadO == "homicidio":
        resultado = "Delacao concedida."
    else:
        resultado = "Delacao rejeitada."

if (delator == "roubo" or delator == "trafico") and DelatadO == "homicidio":
    if DelatadO == "homicidio":
        resultado = "Delacao concedida."
    else:
        resultado = "Delacao rejeitada."
        
print (resultado)