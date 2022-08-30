#----------------------------------HA_LACO--------------------------------------------------------
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        tem_laco = False  # guarda se existe laço
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():  # verifica se o os vertices são iguais dentro de uma aresta
                tem_laco = True  # se forem iguais ha_laco muda pra True (verdadeiro)
            else:
                pass

        return tem_laco  # retorna tem_laco (False/True)
    #------------------------------------//// Fim da função \\\\-------------------------------------
