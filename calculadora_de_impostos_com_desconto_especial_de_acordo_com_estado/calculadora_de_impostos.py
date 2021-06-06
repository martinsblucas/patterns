from orcamento import Orcamento, Item


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
        
    orcamento.aplicar_desconto_especial()
    print(f'Desconto especial aplicado sobre orçamento EM APROVAÇÃO de {orcamento.valor}: {orcamento.desconto_especial}')
    
    orcamento.aprovar()
    orcamento.aplicar_desconto_especial()
    print(f'Desconto especial aplicado sobre orçamento APROVADO de {orcamento.valor}: {orcamento.desconto_especial}')
    
    orcamento.finalizar()
