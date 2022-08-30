#----------------------------------DIJKSTRA_DRONE--------------------------------------------------------

"""
    implementação do algoritmo de dijkstra
"""
    def dijkstra(self, vi, vf): # vi = vertice inicial ,  vf = vertice final

        INFINITO = math.inf
        NAO_VISITADO = 0
        VISITADO = 1
        VI_INICIA_ZERO = 0
        PREDECESSOR_VAZIO = "-"
        VI_PREDECESSOR = "VAZIO"

        vs_do_grafo = self.N # guarda os vertices do grafo
        vs_do_grafo.sort()

        arestas_visitadas = []

        # construindo os dicionários ----------------------
        arr1 = []
            #menor_caminho
        for v in vs_do_grafo:
            lista1 = (v, INFINITO)
            arr1.append(lista1)
        menor_caminho = dict(arr1) # armazena menor caminho até o vértice

        arr2 = []
            #v_visitados
        for v in vs_do_grafo:
            lista2 = (v, NAO_VISITADO)
            arr2.append(lista2)
        v_visitados = dict(arr2) # armazena os vertices visitados após visitar todos os adjacentes

        arr3 = []
            #predecessores
        for v in vs_do_grafo:
            lista3 = (v, PREDECESSOR_VAZIO)
            arr3.append(lista3)
        predecessores = dict(arr3) # armazena o predecessor ddo vertice visitado

        # ------------------------------------------


        # execução
        v_atual = vi  # guarda vertice atual

        while v_atual != vf: # enquanto v_atual for diferente de vf

            if v_atual == vi: # se v_atual == vi -------------------------------------------------------------
                menor_caminho[v_atual] = VI_INICIA_ZERO # vi recebe o valor 0
                vertices_adj = self.vertices_adj_V(v_atual)
                for v_adj in (vertices_adj): # percorre os vertices adjacentes a v_atual
                    aresta = self.arestas_de_V_v2(v_adj, v_atual) # recupera a aresta de v_atual e vi
                    peso_beta = self.A[aresta].getPeso()
                    menor_caminho[v_adj] = peso_beta # o peso da aresta
                    predecessores[v_adj] = v_atual

                v_visitados[v_atual] = VISITADO # vi marcado como visitado
                predecessores[v_atual] = VI_PREDECESSOR

                # encontrando menor entre os betas que não foi visitado para o proximo v_atual
                beta = INFINITO
                vadj = ""
                for v_adj in (self.vertices_adj_V(v_atual)):  # percorre os vertices adjacentes a v_atual
                    if v_visitados[v_adj] == NAO_VISITADO:
                        if (menor_caminho[v_adj] < beta):
                            beta = menor_caminho[v_adj]
                            vadj = v_adj
                v_atual = vadj # atualizando v_atual pelo menores entre os betas não visitados

            else:
                v_visitados[v_atual] = VISITADO
                vertices_adj_v_atual = self.vertices_adj_V(v_atual) # guarda vertices adjacentes a v_atual

                vertices_menores_caminhos = []
                for v in (vertices_adj_v_atual):  # percorre os vertices adjacentes a v_atual
                    aresta = self.arestas_de_V_v2(v_atual, v)  # recupera a aresta de vadj e v_atual
                    soma = (menor_caminho[v_atual] + self.A[aresta].getPeso())
                    if v_visitados[v] == NAO_VISITADO: # se v não foi visitado
                        if (menor_caminho[v] > soma): # se o caminho de V for maior que a soma
                            menor_caminho[v] = soma # soma é atribuido ao caminho de v
                            predecessores[v] = v_atual # v recebe como seu predecessor v_atual
                            vertices_menores_caminhos.append(v)

                # encontrando menor entre os betas que não foi visitado para o proximo v_atual
                beta = INFINITO
                vadj = ""
                for v_adj in vertices_menores_caminhos: #percorre os vertices adjacentes a v_atual e compara valores de menor_caminho
                    if v_visitados[v_adj] == NAO_VISITADO:
                        if (menor_caminho[v_adj] < beta):
                            beta = menor_caminho[v_adj]
                            vadj = v_adj

                v_atual = vadj # atualizando v_atual pelo menores entre os betas não visitados


        #retornando o menor caminho
        menor_caminho_final = [] # guarda o menor caminho

        v_ant = vf
        menor_caminho_final.append(vf)  # adiciona vf a lista
        while v_ant != vi: # para o laço quando vi for encontrando
            menor_caminho_final.append(predecessores[v_ant]) # adiciona os antecessores
            #menor_caminho_final.append("-") # separador
            v_ant = predecessores[v_ant]

        return (list(reversed(menor_caminho_final))) # retorna a lista final com o menor caminho

    #------------------------------------//// Fim da função \\\\-------------------------------------
