#----------------------------------BFS--------------------------------------------------------
    def bfs(self, V=''):
        '''
            Busca Por Largura (Breadth-First Search - BFS)
            Percorre o grafo e retorna um sub_grafo que contem todos os vertices e a arestas percorridas no caminho realizado,
        forma a arvore a partir das arestas de cada vertice pai e escolhe um vertice filho para continuar a arovore até que
        todos os vertices tenham sido acrescentados a arvore.
        '''

        sub_grafo = MeuGrafo()# objeto de retorno, grafo final
        a_visitadas = set()  # Arestas visitadas
        vertice_raiz = [V] # Guarda os vertices passados como raiz

        def bfs_secundaria(self, v1, vertice_raiz):  # função recursiva

            # VARIAVEIS
            #-----------------------------
            vz = vertice_raiz[-1] # recebe o vertice pai
            global v2  # variavel global, guarda o valor do vertice oposto
            arestas = (self.arestas_sobre_vertice(v1))  # arestas sobre o vertice v1
            arestas_ordenadas = [] # listas de auxilio para ordenação
            arestas_de_v = [] # lista final
            # -----------------------------//

            # ORDENAÇÃO, FORMTAÇÃO DA LISTA DAS ARESTAS PARA VERIFICAÇÃO
            # -----------------------------
            for i in arestas:
                arestas_ordenadas.append(i[1:])
            arestas_ordenadas = sorted(map(int, arestas_ordenadas)) # ordenação
            for i in arestas_ordenadas: # FORMATAÇÃO DAS STRINGS DAS ARESTAS: "a1", "a2"..."a13"
                a = 'a' + str(i)
                arestas_de_v.append(a) # lista final com as arestas ordenadas e formatadas
            # -----------------------------//

            # VERIFICAÇÃO DAS ARESTAS DE V1
            # -----------------------------
            if v1 not in sub_grafo.N:  # se V não estiver em sub_grafo
                sub_grafo.adicionaVertice(v1)  # adiciona V no sub_grafo

            todas_arestas_foram_visitadas = True # guarda a informação se todas as arestas do v1 foram visitadas ou não

            for a in arestas_de_v:
                if a not in a_visitadas:
                    todas_arestas_foram_visitadas = False
                    break

            if todas_arestas_foram_visitadas == True: # Se todas as arestas de v1 foram visitadas
                v1 = vz # v1 recebe o vertice pai
                vertice_raiz.pop() # o Vertice pai é deletado
                bfs_secundaria(self, v1, vertice_raiz)  # chamada recursiva para retornar ao vertice pai (raiz)
            # -----------------------------//

            # PERCORRENDO AS ARESTAS E ATRIBUINDO OS VALORES NAS VARIAVEIS
            # -----------------------------
            for aresta_atual in arestas_de_v:  # percorrendo a lista de arestas sobre o vertice V

                if aresta_atual not in a_visitadas:  # se a aresta atual não tiver sido visitada
                    a_visitadas.add(aresta_atual)  # adiciona aresta atual a lista de arestas visitadas

                    if v1 == self.A[aresta_atual].getV1():  # se V for iguala a getV1 da aresta atual
                        v2 = self.A[aresta_atual].getV2()  # adicona o valor de getV2 a v2
                    else:
                        v2 = self.A[aresta_atual].getV1()  # caso o valor seja igual a getV2 da aresta adicona esse valor a v2

                    if v2 not in sub_grafo.N:  # verificando se v2 está no sub_grafo
                        sub_grafo.adicionaVertice(v2)  # adiciona v2 a sub_grafo
                        vertice_raiz.append(v2) # adiciona v2 a lista de vertice_raiz
                        sub_grafo.adicionaAresta(aresta_atual, self.A[aresta_atual].getV1(),self.A[aresta_atual].getV2()) # adiciona a aresta a partir do grafo original
            # -----------------------------//

            # VERIFICANDO SE TODOS OS NÓS (VERTICES) FORAM VISITADOS
            # -----------------------------
            if (sorted(sub_grafo.N) != sorted(self.N)):  # caso todos os vertices não tenham sido visitados
                vertice_raiz.append(v1) # adicona v1 a lista de vertice_raiz
                bfs_secundaria(self, v2, vertice_raiz)  # chamada recursiva com v2 como próximo vertice a ser analisado

            else:  # caso todos os vertices já tenham sidos visitados
                return #encerra bfs_secundaria
            # -----------------------------//

        bfs_secundaria(self, V, vertice_raiz)  # primeira chamada da bfs_secundaria

        # retorna sub_grafo e encerra o programa
        return sub_grafo
    #------------------------------------//// Fim da função \\\\-------------------------------------
