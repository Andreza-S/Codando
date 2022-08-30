# ----------------------------------retorna_vertice_adj-------------------------------------------------------------
    '''
        Retorna o vertice adjacente a v contido na aresta
    '''
    def retorna_vertice_adj(self, v, aresta):
        vert_ajd = ""

        if self.A[aresta].getV1() != v:
            vert_ajd = self.A[aresta].getV1()
        else:
            vert_ajd = self.A[aresta].getV2()

        return vert_ajd
    # ------------------------------------//// Fim da função \\\\-------------------------------------
