def vertices_nao_adjacentes(self):
    '''
    Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
    Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
    :return: Uma lista com os pares de vértices não adjacentes
    '''
    # fazer dois for guardando Ns
    # percorrer as arestas para verificar se o par existe ou nâo

    lista_no_nao_adj = set()


    for i in range (len(self.M)):
        for j in range (i+1, len(self.M)):
            if self.M[i][j] == {}:
                par_validado = str(self.N[i] + "-" + self.N[j])
                lista_no_nao_adj.add(par_validado)

        for a in range(i):
            if self.M[a][i] == {}:
                par_validado = str(self.N[i] + "-" + self.N[a])
                lista_no_nao_adj.add(par_validado)



    return lista_no_nao_adj  # retorna a lista
#__________________________________________________FIM________________________________________________________

def ha_laco(self):
    '''
    Verifica se existe algum laço no grafo.
    :return: Um valor booleano que indica se existe algum laço.
    '''
    for i in range(len(self.M)):
        if len(self.M[i][i]) > 0:
            return True
    return False

# __________________________________________________FIM________________________________________________________

def grau(self, V=''):
    '''
    Provê o grau do vértice passado como parâmetro
    :param V: O rótulo do vértice a ser analisado
    :return: Um valor inteiro que indica o grau do vértice
    :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''

    if V not in self.N:
        raise VerticeInvalidoException("O vértice não existe no grafo")

    grau = 0
    indice_v = self.N.index(V)

    for i in range (indice_v,len(self.M)): # muda-se a coluna
        if len(self.M[indice_v][i]) > 0:
            if i == indice_v: # se houver laço
                grau += 2* len(self.M[indice_v][i])
            else:
                grau += len(self.M[indice_v][i])

    for j in range (0, indice_v): # muda-se as linhas
        if len(self.M[j][indice_v]) > 0:
            grau += len(self.M[j][indice_v])

    return grau

# __________________________________________________FIM________________________________________________________

def ha_paralelas(self):
    '''
    Verifica se há arestas paralelas no grafo
    :return: Um valor booleano que indica se existem arestas paralelas no grafo.
    '''
    for i in range(len(self.M)):
        for j in range(len(self.M)):
            if len(self.M[i][j]) > 1:
                return True
    return False

# __________________________________________________FIM________________________________________________________

def arestas_sobre_vertice(self, V):
    '''
    Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
    :param V: O vértice a ser analisado
    :return: Uma lista os rótulos das arestas que incidem sobre o vértice
    :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''

    if V not in self.N:
        raise VerticeInvalidoException("O vértice não existe no grafo")  # tratamento para excessao

    indice_v = self.N.index(V)
    lista_arestas_sobre_vertice = set()  # lista das arestas sobre o vertice

    for i in range (indice_v,len(self.M)): # muda-se a coluna
        if len(self.M[indice_v][i]) > 0:
            arestas = self.M[indice_v][i]
            for a in arestas:
                lista_arestas_sobre_vertice.add(a)

    for j in range (0, indice_v): # muda-se as linhas
        if len(self.M[j][indice_v]) > 0:
            arestas = self.M[j][indice_v]
            for a in arestas:
                lista_arestas_sobre_vertice.add(a)

    return lista_arestas_sobre_vertice  # retorna lista_arestas_sobre_vertice

# __________________________________________________FIM________________________________________________________

def eh_completo(self):
    '''
    Verifica se o grafo é completo.
    :return: Um valor booleano que indica se o grafo é completo
    '''
    eh_grafo_completo = False

    # Um grafo completo tem que ser um grafo SIMPLES e TODOS os nós estao conectados entre si
    # dois passos para validação


    # criacao das variaveis
    qtd_de_arestas_no_grafo = 0
    qtd_de_vertices_no_grafo = len(self.N)

    #conta a quantidade de arestas no grafo
    for i in range (len(self.M)):
        for j in range (i, len(self.M)):
            if len(self.M[i][j]) > 0:
                qtd_de_arestas_no_grafo += 1

    # essa formula ((n(n-1)/2) *n é a qtd_de_vertices) é utilizada para verificar
    # a quantidade de arestas necessarias para o grafo ser completo
    # após a validação de ser um grafo simples
    formula_grafo_completo = (qtd_de_vertices_no_grafo * (qtd_de_vertices_no_grafo - 1)) / 2

    # 1o verificar se o grafo é simples
    if self.ha_paralelas() == False:  # verifica se tem arestas paralelas(se tiver nao é simples)
        if self.ha_laco() == False:  # verifica se tem laco (se tiver nao é simples)

            # se for simples:

            # 2o verificar se a quantidade de arestas é igual a formula do grafo completo
            # (informação extraida de: https://www.pucsp.br/~jarakaki/grafos/Aula2.pdf ,
            # https://pt.wikipedia.org/wiki/Grafo_completo ,
            # https://miltonborba.org/Algf/Grafos.htm#:~:text=Um%20grafo%20completo%20com%20v,prova%20%C3%A9%20por%20indu%C3%A7%C3%A3o%20matem%C3%A1tica.)

            if qtd_de_arestas_no_grafo == formula_grafo_completo:
                eh_grafo_completo = True

    return eh_grafo_completo  # retorna eh_grafo_completo (False/True)

# __________________________________________________FIM________________________________________________________
