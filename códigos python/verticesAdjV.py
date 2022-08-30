#----------------------------------VERTICES_ADJ_V--------------------------------------------------------
"""
    RECEBE UM GRAFO E UM VERTICE (V)
    RETORNA UMA LISTA COM OS VERTICESS ADJACENTES A V
"""
    def vertices_adj_V(self, V):
        lista_adjacentes = []

        aresta_sobre_V = self.arestas_sobre_vertice(V)

        for a in aresta_sobre_V:  # percorrendo as arestas e verificando os pares de vertices
            if V == self.A[a].getV1():  # se for igual a V1
                lista_adjacentes.append(self.A[a].getV2())  # adiciona o V2 (vertice oposto)
            if V == self.A[a].getV2():  # se for igual a V2
                lista_adjacentes.append(self.A[a].getV1())  # adicona V1 (vetrice oposto)

        return lista_adjacentes  # retorna a lista dos vertice adjacentes
    #------------------------------------//// Fim da função \\\\-------------------------------------
