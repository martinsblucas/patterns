class DescontoPorMaisDeCincoItens:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        return orcamento.valor * 0.05 if orcamento.total_itens > 5 else self.__proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        return orcamento.valor * 0.07 if orcamento.valor > 500 else self.__proximo_desconto.calcula(orcamento)


class SemDesconto:
    def calcula(self, orcamento):
        return 0
