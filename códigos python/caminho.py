#----------------------------------CAMINHO--------------------------------------------------------

"""
    retorna false caso não exista caminho
    retorna o subgrafo caso exista caminho com o caminho de tamanho n
""" 
    def caminho(self, n):
        for v in self.N: # percorre a lista de vertices do grafo recebido
            sub_grafo = self.bfs(v) # guarda o sub_grafo recebido de bfs
            if len(sub_grafo.A) == n: # verifica s eos tamanhos são iguais
                return sub_grafo # se forem retorna o sub_grafo
        return False # caso contrário retorna False

    #------------------------------------//// Fim da função \\\\-------------------------------------
