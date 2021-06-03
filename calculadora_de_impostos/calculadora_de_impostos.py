from impostos import ISS, ICMS


class CalculadoraDeImpostos:
    def __init__(self):
        self.__imposto_calculado = 0
    
    def realiza_calculo(self, orcamento, imposto):
        self.__imposto_calculado = imposto.calcular(orcamento)

    @property
    def imposto_calculado(self):
        return self.__imposto_calculado

    def imprime_imposto_calculado(self):
        print(self.__imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = CalculadoraDeImpostos()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento, ISS())
    calculador.imprime_imposto_calculado()
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.imprime_imposto_calculado()
