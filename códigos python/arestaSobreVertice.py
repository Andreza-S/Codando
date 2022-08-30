#----------------------------------ARESTAS_SOBRE_VERTICE--------------------------------------------------------
    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N:
            raise VerticeInvalidoException("O vértice não existe no grafo")  # tratamento para excessao

        lista_arestas_sobre_vertice = set()  # lista das arestas sobre o vertice

        for j in self.A:
            if (V == self.A[j].getV1()):  # se for igual é adicionado na lista o rotulo
                lista_arestas_sobre_vertice.add(j)
            if (V == self.A[j].getV2()):  # sse for igual é adicionado na lista o rotulo
                lista_arestas_sobre_vertice.add(j)

        return lista_arestas_sobre_vertice  # retorna lista_arestas_sobre_vertice
    #------------------------------------//// Fim da função \\\\-------------------------------------
