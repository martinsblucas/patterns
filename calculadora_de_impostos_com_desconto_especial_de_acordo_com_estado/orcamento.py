from abc import ABC, abstractmethod


class EstadoDeOrcamento(ABC):
    @abstractmethod
    def aplicar_desconto_especial(self, orcamento):
        pass
    
    @abstractmethod
    def aprovar(self, orcamento):
        pass
    
    @abstractmethod
    def reprovar(self, orcamento):
        pass
    
    @abstractmethod
    def finalizar(self, orcamento):
        pass


class Aprovado(EstadoDeOrcamento):
    def aplicar_desconto_especial(self, orcamento):
        orcamento.incrementar_em_desconto_especial(orcamento.valor * 0.05)
    
    def aprovar(self, orcamento):
        raise Exception('Não pode aprovar orçamento aprovado')
    
    def reprovar(self, orcamento):
        raise Exception('Não pode reprovar orçamento aprovado')
    
    def finalizar(self, orcamento):
        orcamento.estado_atual = Finalizado()


class EmAprovacao(EstadoDeOrcamento):
    def aplicar_desconto_especial(self, orcamento):
        orcamento.incrementar_em_desconto_especial(orcamento.valor * 0.02)
    
    def aprovar(self, orcamento):
        orcamento.estado_atual = Aprovado()
    
    def reprovar(self, orcamento):
        orcamento.estado_atual = Reprovado()
    
    def finalizar(self, orcamento):
        raise Exception('Não pode finalizar orçamento em aprovação')


class Reprovado(EstadoDeOrcamento):
    def aplicar_desconto_especial(self, orcamento):
        raise Exception('Nao pode aplicar desconto especial em orçamento reprovado')
    
    def aprovar(self, orcamento):
        raise Exception('Não pode aprovar orçamento reprovado')
    
    def reprovar(self, orcamento):
        raise Exception('Não pode reprovar orçamento reprovado')
    
    def finalizar(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoDeOrcamento):
    def aplicar_desconto_especial(self, orcamento):
        raise Exception('Nao pode aplicar desconto especial em orçamento finalizado')
    
    def aprovar(self, orcamento):
        raise Exception('Não pode aprovar orçamento finalizado')
    
    def reprovar(self, orcamento):
        raise Exception('Não pode reprovar orçamento finalizado')
    
    def finalizar(self, orcamento):
        raise Exception('Não pode finalizar orçamento finalizado')


class Orcamento:
    def __init__(self):
        self.__itens = []
        self.__estado_atual = EmAprovacao()
        self.__desconto_especial = 0
        
    @property
    def valor(self):
        return sum(item.valor for item in self.__itens)

    @property
    def itens(self):
        return self.__itens[:]

    @property
    def total_itens(self):
        return len(self.itens)
    
    @property
    def estado_atual(self):
        return self.__estado_atual
        
    @estado_atual.setter
    def estado_atual(self, valor):
        self.__estado_atual = valor
        
    @property
    def desconto_especial(self):
        return self.__desconto_especial
        
    def incrementar_em_desconto_especial(self, valor):
        self.__desconto_especial += valor
        
    def aplicar_desconto_especial(self):
        self.__estado_atual.aplicar_desconto_especial(self)
    
    def aprovar(self):
        self.__estado_atual.aprovar(self)
    
    def reprovar(self):
        self.__estado_atual.reprovar(self)
    
    def finalizar(self):
        self.__estado_atual.finalizar(self)

    def adicionar_item(self, item):
        self.__itens.append(item)


class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor
