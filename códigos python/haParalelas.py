#----------------------------------HA_PARALELAS--------------------------------------------------------
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        # percorre as arestas e checa se existem arestas com os vertices iguais

        ha_paralelas = False  # variavel de controle para true ou false
        # tamanho_A = len(self.A) # tamanho da lista Arestas

        for i in self.A:  # percorrer aresta 1
            if ha_paralelas == False:

                for j in self.A:  # aresta 2
                    if (j == i):  # se for igual, vá para a próxima interação
                        continue
                    else:
                        if (self.A[i].getV1() == self.A[
                            j].getV1()):  # X-J   Verifica as possibilidades dos nós serem iguais
                            if (self.A[i].getV2() == self.A[j].getV2()):  # X-J
                                ha_paralelas = True
                                break
                        else:
                            if (self.A[i].getV1() == self.A[j].getV2()):  # J-X verifica a possibilidade invertida
                                if (self.A[i].getV2() == self.A[j].getV1()):  # J-X
                                    ha_paralelas = True
                                    break
            else:
                break
        return ha_paralelas  # retorna ha_paralela (False/True)
    #------------------------------------//// Fim da função \\\\-------------------------------------
