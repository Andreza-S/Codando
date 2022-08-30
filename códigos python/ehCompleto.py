#----------------------------------EH_COMPLETO--------------------------------------------------------
    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        eh_grafo_completo = False

        # Um grafo completo tem que ser um grafo SIMPLES e TODOS os nós estao conectados entre si
        # dois passos para validação

        # criacao das variaveis
        qtd_de_arestas_no_grafo = len(self.A)
        qtd_de_vertices_no_grafo = len(self.N)

        # essa formula ((n(n-1)/2) *n é a qtd_de_vertices) é utilizada para verificar
        # a quantidade de arestas necessarias para o grafo ser completo
        # após a validação de ser um grafo simples
        formula_grafo_completo = (qtd_de_vertices_no_grafo * (qtd_de_vertices_no_grafo - 1)) / 2

        # 1o verificar se o grafo é simples
        if self.ha_paralelas() == False:  # verifica se tem arestas paralelas(se tiver nao é simples)
            if self.ha_laco() == False:  # verifica se tem laco (se tiver nao é simples)

                # se for simples:

                # 2o verificar se a quantidade de arestas é igual a formula do grafo completo
                # (informação extraida de: https://www.pucsp.br/~jarakaki/grafos/Aula2.pdf ,
                # https://pt.wikipedia.org/wiki/Grafo_completo ,
                # https://miltonborba.org/Algf/Grafos.htm#:~:text=Um%20grafo%20completo%20com%20v,prova%20%C3%A9%20por%20indu%C3%A7%C3%A3o%20matem%C3%A1tica.)

                if qtd_de_arestas_no_grafo == formula_grafo_completo:
                    eh_grafo_completo = True

        return eh_grafo_completo  # retorna eh_grafo_completo (False/True)
    #------------------------------------//// Fim da função \\\\-------------------------------------
