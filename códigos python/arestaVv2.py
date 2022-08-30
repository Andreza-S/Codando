#----------------------------------ARESTAS_DE_V_V2--------------------------------------------------------
    """
        RECEBE DOIS VERTICES
        RETORNA A ARESTA QUE CONTEM AMBOS OS VERTICES NO GRAFO
    """
    def arestas_de_V_v2(self, V, v2):
        # Procuro a aresta de acordo com os vértices passados
        for aresta in self.A.values():
            if (V == aresta.getV1() and v2 == aresta.getV2()) or (v2 == aresta.getV1() and V == aresta.getV2()):  # Pegar os vértices da seguinte forma: ex "J-C" OU "C-J"
                aresta_V_v2 = aresta.getRotulo()

                return aresta_V_v2
    #------------------------------------//// Fim da função \\\\-------------------------------------
