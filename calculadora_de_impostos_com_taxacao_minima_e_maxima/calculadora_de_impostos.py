from orcamento import Orcamento, Item
from impostos import ISS, ICMS, IOF, IPI


class CalculadoraDeImpostos:
    def __init__(self):
        self.__imposto_calculado = 0
    
    def realiza_calculo(self, orcamento, imposto):
        self.__imposto_calculado = imposto.calcular(orcamento)

    @property
    def imposto_calculado(self):
        return self.__imposto_calculado


if __name__ == '__main__':
    itens = [{'nome': 'Item 1', 'valor': 100}, 
             {'nome': 'Item 2', 'valor': 50}, 
             {'nome': 'Item 3', 'valor': 400}]
    itens = [Item(**args) for args in itens]
    orcamento = Orcamento()
    for item in itens:
        orcamento.adicionar_item(item)
        
    calculadora = CalculadoraDeImpostos()
    
    print('ISS')
    calculadora.realiza_calculo(orcamento, ISS())
    print(calculadora.imposto_calculado)
    
    print('ICMS')
    calculadora.realiza_calculo(orcamento, ICMS())
    print(calculadora.imposto_calculado)
    
    print('IOF')
    calculadora.realiza_calculo(orcamento, IOF())
    print(calculadora.imposto_calculado)
    
    print('IPI')
    calculadora.realiza_calculo(orcamento, IPI())
    print(calculadora.imposto_calculado)
