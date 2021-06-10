from datetime import date
from .observadores import imprime, salva_no_banco, envia_por_email


class NotaFiscal:
    def __init__(self, razao_social, data_de_emissao, cnpj, itens, detalhes, observadores=[imprime, salva_no_banco, envia_por_email]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        self.__itens = itens
        for observador in observadores:
            observador(self)
        
    @property
    def razao_social(self):
        return self.__razao_social
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def data_de_emissao(self):
        return self.__data_de_emissao
    
    @property
    def detalhes(self):
        return self.__detalhes
    
    @property
    def itens(self):
        return self.__itens[:]


if __name__ == '__main__':
    nota_fiscal = NotaFiscal(razao_social='Builder SA', 
                             cnpj='07800459000119', 
                             detalhes='Detalhes e mais detalhes', 
                             itens=['item1', 'item2', 'item3'],
                             data_de_emissao=date.today(), 
                             observadores=[imprime, envia_por_email, salva_no_banco])
