#----------------------------------VERTICES_NAO_ADJACENTES--------------------------------------------------------
    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        # fazer dois for guardando Ns
        # percorrer as arestas para verificar se o par existe ou nâo

        lista_no_nao_adj = set()

        for i in self.N:  # Nó 1
            for j in self.N:  # Nó 2
                if (i != j):  # Se Nó 1 e Nó 2 forem diferentes
                    achei = False  # Variavel de controle, de verificação , achei os vertices Nó1 e Nó2 em uma aresta
                    for k in self.A:  # Percorre a lista de Arestas
                        if (i == self.A[k].getV1() and j == self.A[k].getV2()) or (
                                j == self.A[k].getV1() and i == self.A[
                            k].getV2()):  # verifica as possibilidadse de combinacoes
                            achei = True  # Se eles forem adjacentes, então achei é True

                    if not achei:  # Se achei for False
                        par_validado = str(i + "-" + j)  # Variavel para concatenação
                        lista_no_nao_adj.add(
                            par_validado)  # Adiciona o par a lista de nos nao adj, já no formato padrao

        return lista_no_nao_adj  # retorna a lista
    #------------------------------------//// Fim da função \\\\-------------------------------------
