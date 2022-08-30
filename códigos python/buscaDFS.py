#----------------------------------DFS--------------------------------------------------------
    def dfs(self, V=''):

        '''
        Busca em profundidade (Depth-first search - DFS)
            Percorre o grafo e retorna um sub_grafo que contem todos os vertices e a arestas percorridas no caminho realizado,
        forma a arvore a partir de um vertice raiz e percorre o grafo até que todos os vertices tenham sido acrescentandos
        a arvore.
        '''

        # objeto de retorno, grafo final
        sub_grafo = MeuGrafo()
        v_visitados = set()  # Vertices visitados
        a_visitadas = set() # Arestas visitadas

        def dfs_secundaria(self, V): #função recursiva

            # VARIAVEIS
            # -----------------------------
            global v2 # variavel global, guarda o valor do vertice oposto
            arestas = (self.arestas_sobre_vertice(V))  # ordenação da lista de arestas
            arestas_ordenadas = []
            arestas_de_v = []
            # -----------------------------//

            # ORDENA E FORMATA A LISTA DE ARESTAS DE V
            # -----------------------------
            for i in arestas:
                arestas_ordenadas.append(i[1:])
            arestas_ordenadas = sorted(map(int, arestas_ordenadas))

            for i in arestas_ordenadas:
                a = 'a' + str(i)
                arestas_de_v.append(a)
            # -----------------------------//

            # PERCORRENDO AS ARESTAS DE V E ATRIBUINDO OS VALORES AS VARIAVEIS
            # -----------------------------
            for aresta_atual in arestas_de_v: # percorrendo a lista de arestas sobre o vertice V

                if aresta_atual not in a_visitadas: # se a aresta atual não tiver sido visitada

                    if V not in v_visitados: # se o vértice (nó) V não tiver sido visitado
                        v_visitados.add(V) # adiciona V a lista de visitados

                    if V not in sub_grafo.N: # Caso o vertice V não esteja ainda no sub_grafo (grafo que será retornado)
                        sub_grafo.adicionaVertice(V) # V é adicioando ao sub_grafo

                    if V == self.A[aresta_atual].getV1(): # Se V for igual ao getV1 da aresta_atual
                        v2 = self.A[aresta_atual].getV2() # V2 recebe o valor do getV2 pertencente a aresta atual

                        if v2 not in sub_grafo.N: # se V2 não estiver incluido no sub_grafo
                            a_visitadas.add(aresta_atual)  # adicona aresta atual a lista de arestas visitadas
                            sub_grafo.adicionaVertice(v2) # adiciona V2 ao sub_grafo
                            sub_grafo.adicionaAresta(aresta_atual, self.A[aresta_atual].getV1(), self.A[aresta_atual].getV2()) # adiciona a aresta a sub_grafo
                            break
                        else:
                            continue # Se V já estiver em sub_grafo, força a proxima interação do loop para a proxima aresta
                    else: # caso V seja igual a getV2 da aresta_atual
                        v2 = self.A[aresta_atual].getV1() # V2 recebe o valor de getV1 da aresta_atual
                        if v2 not in sub_grafo.N: # se v2 não estiver em sub_grafo
                            sub_grafo.adicionaVertice(v2) #adicona v2 a sub_grafo
                            sub_grafo.adicionaAresta(aresta_atual, self.A[aresta_atual].getV1(), self.A[aresta_atual].getV2()) #adicona a aresta_atual a sub_grafo
                            break
                        else:
                            continue # Se V já estiver em sub_grafo, força a proxima interação do loop para a proxima aresta
                else:
                    continue # caso a aresta_atual já tenha sido visitada
            # -----------------------------//

            # ANALISANDO SE TODOS OS NÓS (VERTICES) FORAM VISITADOS
            # -----------------------------
            if (sorted(sub_grafo.N) != sorted(self.N)): # caso todos os vertices não tenha sido visitados
                dfs_secundaria(self, v2) # chamada recursiva
            else: # caso todos os vertices já tenham sidos visitados encerra dfs_secundaria
                return
            # -----------------------------//

        dfs_secundaria(self, V) # primeira chamada da dfs_secundaria

        # retorna sub_grafo e encerra o programa
        return sub_grafo
    #------------------------------------//// Fim da função \\\\-------------------------------------

