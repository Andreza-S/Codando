"""Descrição
A Entidade ganhou n cubos, e decidiu fazer uma pirâmide com eles. Ela quer construir seguindo o seguinte padrão: o topo deve conter 1 cubo, segundo nível deve conter 1 + 2 = 3 cubos, o terceiro nível deve conter 1 + 2 + 3 = 6 cubos e assim por diante. Dessa forma, o i-ésimo nível da pirâmide deve conter 1 + 2 + ... + (i - 1) + i cubos.

A Entidade quer saber qual é a altura máxima que ela pode construir usando os n cubos.

Observação: A Entidade não pode construir um pedaço de um nível; ou ela contrói todo ou ela não constrói.

Formato de entrada

A única linha da entrada contém um inteiro n, representando a quantidade de cubos que a Entidade ganhou.

Formato de saída

Imprima um inteiro representando a maior altura possível da pirâmide."""



num_cubos = int (input())
cubos_usados = 0
nivel =0

while num_cubos - cubos_usados >= (nivel*(1+nivel))/2:
    cubos_usados += (nivel*(1+nivel))/2
    nivel += 1

print (nivel-1)