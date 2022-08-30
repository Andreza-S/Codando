# ----------------------------------PRIM-------------------------------------------------------------
    def prim(self, vi):  # vi = vertice inicial
        '''
        DADO UM VERTICE PERTECENTE AO GRAFO
        RETORNA UMA LISTA CONTENDO AS ARESTA DO MENOR SUBGRAFO COM A MENOR SOMA DE PESOS DESSAS
        '''

        INFINITO = math.inf

        arvore = [] # v1-a1-v2... recebe os nós e as arestas que compoem a arvore final (sub-grafo)

        vertices_visitados = {vi} # guarda os vertices visitados
        vertices_grafo = self.N # guarda os vertices do grafo

        vertices_visitados_final = []

        arestas_visitadas = [] # guarda arestas já visitadas

        aresta_menor_peso = "" # guarda o rótulo da aresta com o menor peso
        menor_peso = INFINITO # guarda o valor da aresta com o menor peso

        while vertices_grafo != vertices_visitados_final:

            aresta_menor_peso = ""
            menor_peso = INFINITO

            for vertice in vertices_visitados:
                arestas_de_vertice = self.arestas_sobre_vertice(vertice)
                for aresta in arestas_de_vertice:
                    if aresta not in arestas_visitadas:
                        peso_aresta = self.A[aresta].getPeso()
                        if peso_aresta < menor_peso:
                            menor_peso = self.A[aresta].getPeso()
                            aresta_menor_peso = aresta

            arestas_visitadas.append(aresta_menor_peso)

            if self.A[aresta_menor_peso].getV1() not in vertices_visitados:
                vertices_visitados.add(self.A[aresta_menor_peso].getV1())
            else:
                vertices_visitados.add(self.A[aresta_menor_peso].getV2())

            vertices_visitados_final = sorted(vertices_visitados)

        for aresta in arestas_visitadas:
            arvore.append(self.A[aresta].getV1())
            arvore.append(aresta)
            arvore.append(self.A[aresta].getV2())

        return arestas_visitadas

    # ------------------------------------//// Fim da função \\\\-------------------------------------
