#----------------------------------HA_CICLOS--------------------------------------------------------

"""
    retorna os ciclos contidos no grafo caso exista alguma
    retorna false caso não exista caminhos no grafo
"""
    def ha_ciclo(self):  # recebe o grafo
        lista_de_ciclos = [] # objeto de retorno

        #----------------------Percorrendo os Vertices do grafo
        for V in self.N:  # percorre os vertices do grafo para verificar a existencia de ciclos para cada V
            if self.grau(V) >=2: # tiver grau igual ou maior que 2

                #----------Variaveis
                arestas_sobre_V = sorted(self.arestas_sobre_vertice(V))
                vertices_adjacentes_V = sorted(self.vertices_adj_V(V))
                #------------//

                #-----------------Lopp percorrendo os vertices adjacentes de v2
                for v2 in vertices_adjacentes_V: # percorrendo os vertices adjacentes a V
                    if self.grau(v2) >= 2: # se o vertice Adajacente a V tiver grau igual ou maior que 2
                        arestas_e_vertices_do_ciclo = []  # criando a lista de cada ciclo
                        arestas_e_vertices_do_ciclo.append(V)  # adicionando V a lista do ciclo que será iniciado
                        arestas_e_vertices_do_ciclo.append(self.arestas_de_V_v2(V, v2))
                        vertices_adj_v2 = sorted(self.vertices_adj_V(v2))
                        eh_lista_completa = False
                        vertices_adjacentes_atual = vertices_adj_v2

                        # -----------Loop montando o ciclo
                        while (True):
                            arestas_e_vertices_do_ciclo.append(v2)

                            for v3 in vertices_adjacentes_atual:  # percorrendo os vetrices adjacentes
                                if self.grau(v3) >= 2:  # se o vertice Adjacente tiver grau igual ou maior que 2
                                    vertices_adj_v3 = sorted(self.vertices_adj_V(v3))  # atualiza a lista de vertices adjacentes

                                    if v3 == V:  # se o v3 atual for igual a V, significa que o ciclo foi enocntrado
                                        verifica_aresta = self.arestas_de_V_v2(v2, V)
                                        if verifica_aresta not in arestas_e_vertices_do_ciclo:
                                            arestas_e_vertices_do_ciclo.append(verifica_aresta)  # adicina a aresta
                                            arestas_e_vertices_do_ciclo.append(v3)  # adicciona o v3
                                            eh_lista_completa = True
                                            break

                                    else:  # caso o v3 não seja igual a V, significa que o ciclo não foi enocntrado ainda
                                        verifica_aresta = (self.arestas_de_V_v2(v2, v3))  # adicionando a aresta
                                        if v3 not in arestas_e_vertices_do_ciclo:
                                            if verifica_aresta not in arestas_e_vertices_do_ciclo:
                                                arestas_e_vertices_do_ciclo.append(verifica_aresta)
                                                v2 = v3  # atualiza v2 para a recursão
                                                vertices_adjacentes_atual = vertices_adj_v3
                                                break


                            if eh_lista_completa:
                                lista_de_ciclos.append(arestas_e_vertices_do_ciclo)  # retorna a lista com os vertices e arestas, finalizando a recursividade
                                break
                        # ------------------//

        #--------Verificando o tamanho da lista de ciclos
        if len(lista_de_ciclos) > 0: # se for maior que 0
            return lista_de_ciclos # retorna a lista_de_ciclos
        else:
            return (False) # caso contrário retorna false, o que significa que não existem ciclos no grafo
    #------------------------------------//// Fim da função \\\\-------------------------------------
