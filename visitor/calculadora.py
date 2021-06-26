from abc import ABC, abstractmethod


class Expressao(ABC):
    @abstractmethod
    def avaliar(self):
        pass
    
    @abstractmethod
    def aceitar(self):
        pass


class Numero(Expressao):
    def __init__(self, valor):
        self.__valor = valor
        
    def avaliar(self):
        return self.__valor
    
    def aceitar(self, visita):
        return visita.numero(visita)

    
class ExpressaoComposta(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita
        
    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita


class Soma(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() + self._expressao_direita.avaliar()
    
    def aceitar(self, visita):
        return visita.soma(self)


class Subtracao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() - self._expressao_direita.avaliar()
    
    def aceitar(self, visita):
        return visita.subtracao(self)


class Multiplicacao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() * self._expressao_direita.avaliar()
    
    def aceitar(self, visita):
        return visita.multiplicacao(self)


class Divisao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() / self._expressao_direita.avaliar()
    
    def aceitar(self, visita):
        return visita.divisao(self)


class Impressao:
    @staticmethod
    def soma(expressao):
        return f'({expressao.expressao_esquerda.avaliar()} + {expressao.expressao_direita.avaliar()})' 
    
    @staticmethod
    def subtracao(expressao):
        return f'({expressao.expressao_esquerda.avaliar()} - {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def multiplicacao(expressao):
        return f'({expressao.expressao_esquerda.avaliar()} * {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def divisao(expressao):
        return f'({expressao.expressao_esquerda.avaliar()} / {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def numero(expressao):
        return expressao.avaliar()


class ImpressaoPrefixa:
    @staticmethod
    def soma(expressao):
        return f'+ ({expressao.expressao_esquerda.avaliar()} {expressao.expressao_direita.avaliar()})' 
    
    @staticmethod
    def subtracao(expressao):
        return f'- ({expressao.expressao_esquerda.avaliar()} {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def multiplicacao(expressao):
        return f'* ({expressao.expressao_esquerda.avaliar()} {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def divisao(expressao):
        return f'/ ({expressao.expressao_esquerda.avaliar()} {expressao.expressao_direita.avaliar()})'
    
    @staticmethod
    def numero(expressao):
        return expressao.avaliar()


if __name__ == '__main__':
    operacao1 = Soma(Numero(100), Numero(100))
    impressao = Impressao()
    impressao_prefixa = ImpressaoPrefixa()
    print('100+100')
    print(operacao1.avaliar())
    print(operacao1.aceitar(impressao))
    print(operacao1.aceitar(impressao_prefixa))
    print('==============================================')
    operacao2 = Subtracao(Numero(700), Numero(200))
    print('700-200')
    print(operacao2.avaliar())
    print(operacao2.aceitar(impressao))
    print(operacao2.aceitar(impressao_prefixa))
    print('==============================================')
    operacao3 = Multiplicacao(Numero(2), Numero(50))
    print('2*50')
    print(operacao3.avaliar())
    print(operacao3.aceitar(impressao))
    print(operacao3.aceitar(impressao_prefixa))
    print('==============================================')
    operacao4 = Divisao(Numero(300), Numero(3))
    print('300/3')
    print(operacao4.avaliar())
    print(operacao4.aceitar(impressao))
    print(operacao4.aceitar(impressao_prefixa))
    print('==============================================')
