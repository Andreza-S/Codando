# ----------------------------------Kruskal -------------------------------------------------------------
        """
           RETORNA UMA LISTA COM AS ARESTA PERTECENTES AO SUBGRAFO COM O MENOR CUSTO DE PESOS
        """
    def kruskal(self):  # vi = vertice inicial

        INFINITO = math.inf
        arvores = sorted(self.N) # cada vertice é uma arvore individual

        arvores_contidas = [] # guarda as arvores já contidas no subgrafo_final

        arestas_nao_contidas = list(self.A) # guarda as arestas não contidas no subgrafo

        subgrafo_final = [] # guarda as arestas do subgrafo final d eretorno da função

        while arvores_contidas != arvores:
            aresta_menor_peso = ""
            peso_aresta = INFINITO

            for aresta in arestas_nao_contidas:
                if self.A[aresta].getPeso() < peso_aresta:
                    aresta_menor_peso = aresta
                    peso_aresta = self.A[aresta].getPeso()

            if (self.A[aresta_menor_peso].getV1() not in arvores_contidas) or (self.A[aresta_menor_peso].getV2() not in arvores_contidas):

                if self.A[aresta_menor_peso].getV1() not in arvores_contidas:
                    arvores_contidas.append(self.A[aresta_menor_peso].getV1())

                if self.A[aresta_menor_peso].getV2() not in arvores_contidas:
                    arvores_contidas.append(self.A[aresta_menor_peso].getV2())

                subgrafo_final.append(aresta_menor_peso)

            arestas_nao_contidas.remove(aresta_menor_peso)
            arvores_contidas = sorted(arvores_contidas)

        return subgrafo_final
    # ------------------------------------//// Fim da função \\\\-------------------------------------