from abc import ABC, abstractmethod


class Imposto(ABC):
    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto
        
    def _calcular_outro_imposto(self, orcamento):
        if not self.__outro_imposto:
            return 0
        return self.__outro_imposto.calcular(orcamento)
    
    @abstractmethod
    def calcular(self, orcamento):
        pass
    

def IPVX(callback):
    def wrapper(self, orcamento):
        return callback(self, orcamento) + 50
    return wrapper


class ISS(Imposto):
    @IPVX
    def calcular(self, orcamento):
        return orcamento.valor * 0.1 + self._calcular_outro_imposto(orcamento)


class ICMS(Imposto):
    def calcular(self, orcamento):
        return orcamento.valor * 0.06 + self._calcular_outro_imposto(orcamento)
    

class ImpostoComMinimaEMaximaTaxacao(Imposto):
    def calcular(self, orcamento):
        valor = self._obter_maxima(orcamento) if self._deve_implementar_maxima(orcamento) else self._obter_minima(orcamento)
        return valor + self._calcular_outro_imposto(orcamento) 
    
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
