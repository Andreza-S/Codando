#----------------------------------GRAU--------------------------------------------------------
    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        grau_do_vertice = 0
        verifica_vertice = self.existeVertice(V)

        if verifica_vertice == True:  # se o vertice existir
            for j in self.A:
                if (V == self.A[j].getV1()):  # se o vertice existir na aresta, grau soma 1
                    grau_do_vertice += 1

                if (V == self.A[j].getV2()):  # se o vertice existir na aresta, grau soma 1
                    grau_do_vertice += 1
        else:
            raise VerticeInvalidoException('O vértice ' + V + ' é inválido')

        return grau_do_vertice  # retorna o valor do grau do vertice
    #------------------------------------//// Fim da função \\\\-------------------------------------
