#----------------------------------CONEXO--------------------------------------------------------

""" 
    verifica se um grafo é conexo ou não
"""
    def conexo(self):
        for v in self.N: # percorre a lista de vertices do graf recebido
            sub_grafo = self.dfs(v) # conexo recebe o sub_grafo a partir de v
            if len(self.N) == len(sub_grafo.N): # se o tamanho da lista de vertices do grafo forem iguais ao de conexo
                return True # retorne verdadeiro para conexo
        return False # caso contrário retornará falso
    #------------------------------------//// Fim da função \\\\-------------------------------------
