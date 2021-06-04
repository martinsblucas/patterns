from abc import ABC, abstractmethod


class ISS:
    def calcular(self, orcamento):
        return orcamento.valor * 0.1


class ICMS:
    def calcular(self, orcamento):
        return orcamento.valor * 0.06
    

class ImpostoComMinimaEMaximaTaxacao(ABC):
    def calcular(self, orcamento):
        return self._obter_maxima(orcamento) if self._deve_implementar_maxima(orcamento) else self._obter_minima(orcamento) 
    
    @abstractmethod
    def _deve_implementar_maxima(self, orcamento):
        pass
    
    @abstractmethod
    def _obter_maxima(self, orcamento):
        pass
    
    @abstractmethod
    def _obter_minima(self, orcamento):
        pass


class IOF(ImpostoComMinimaEMaximaTaxacao):
    def _deve_implementar_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_acima_de_500(orcamento)
    
    def __tem_item_acima_de_500(self, orcamento):
        return any([item.valor > 500 for item in orcamento.itens])
    
    def _obter_maxima(self, orcamento):
        return orcamento.valor * 0.07
    
    def _obter_minima(self, orcamento):
        return orcamento.valor * 0.03


class IPI(ImpostoComMinimaEMaximaTaxacao):
    def _deve_implementar_maxima(self, orcamento):
        return orcamento.valor > 500
    
    def _obter_maxima(self, orcamento):
        return orcamento.valor * 0.05
    
    def _obter_minima(self, orcamento):
        return orcamento.valor * 0.01
