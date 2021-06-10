from .orcamento import Orcamento, Item
from .descontos import DescontoPorMaisDeCincoItens, DescontoPorMaisDeQuinhentosReais, SemDesconto


class CalculadoraDeDescontos:
    def calcula(self, orcamento):
        return DescontoPorMaisDeCincoItens(
            DescontoPorMaisDeQuinhentosReais(
                SemDesconto()
            )
        ).calcula(orcamento)


if __name__ == '__main__':
    itens = [{'nome': 'Item 1', 'valor': 100}, 
             {'nome': 'Item 2', 'valor': 50}, 
             {'nome': 'Item 3', 'valor': 400}]
    itens = [Item(**args) for args in itens]
    orcamento = Orcamento()
    for item in itens:
        orcamento.adicionar_item(item)
    
    calculadora = CalculadoraDeDescontos()
    desconto = calculadora.calcula(orcamento)

    print('-----------------------------------------')
    print('Orçamento')
    print('-----------------------------------------')
    for item in orcamento.itens:
        print(f'Item: {item.nome}')
        print(f'Valor: {item.valor}')
        print('-----------------------------------------')    
    print(f'Valor total do orçamento: {orcamento.valor}')
    print('Valor total do desconto: {:.2f}'.format(desconto))
    print('-----------------------------------------')
