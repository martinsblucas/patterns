from abc import ABC, abstractmethod


class Expressao(ABC):
    @abstractmethod
    def avaliar(self):
        pass
    
    
class Numero(Expressao):
    def __init__(self, valor):
        self.__valor = valor
        
    def avaliar(self):
        return self.__valor
    
    
class ExpressaoComposta(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita


class Soma(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() + self._expressao_direita.avaliar()


class Subtracao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() - self._expressao_direita.avaliar()
    

class Multiplicacao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() * self._expressao_direita.avaliar()


class Divisao(ExpressaoComposta):
    def avaliar(self):
        return self._expressao_esquerda.avaliar() / self._expressao_direita.avaliar()


class CombinacaoDeExpressoes(Expressao):
    def __init__(self, *expressoes):
        self.__expressoes = expressoes
        
    def avaliar(self):
        return sum([expressao.avaliar() for expressao in self.__expressoes])


if __name__ == '__main__':
    operacao1 = Soma(Numero(100), Numero(100))
    print('100+100')
    print(operacao1.avaliar())
    print('==============================================')
    operacao2 = Subtracao(Numero(700), Numero(200))
    print('700-200')
    print(operacao2.avaliar())
    print('==============================================')
    operacao3 = Multiplicacao(Numero(2), Numero(50))
    print('2*50')
    print(operacao3.avaliar())
    print('==============================================')
    operacao4 = Divisao(Numero(300), Numero(3))
    print('300/3')
    print(operacao4.avaliar())
    print('==============================================')
    operacao5 = CombinacaoDeExpressoes(operacao1, operacao2, 
                                       operacao3, operacao4)
    print('Combinação de todas as operações anteriores')
    print(operacao5.avaliar())
