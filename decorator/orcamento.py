class Orcamento:
    def __init__(self):
        self.__itens = []

    @property
    def valor(self):
        return sum(item.valor for item in self.__itens)

    @property
    def itens(self):
        return self.__itens[:]

    @property
    def total_itens(self):
        return len(self.itens)

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
