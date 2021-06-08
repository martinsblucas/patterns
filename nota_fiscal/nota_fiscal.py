from datetime import date


class NotaFiscal:
    def __init__(self, razao_social, data_de_emissao, cnpj, itens, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        self.__itens = itens
        
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
    
    
class GeradorDeNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = []

    def com_razao_social(self, valor):
        self.__razao_social = valor
        return self
    
    def com_cnpj(self, valor):
        self.__cnpj = valor
        return self
    
    def com_data_de_emissao(self, valor):
        self.__data_de_emissao = valor
        return self
    
    def com_detalhes(self, valor):
        self.__detalhes = valor
        return self
        
    def com_itens(self, valor):
        self.__itens = valor
        return self
    
    def constroi(self) -> NotaFiscal:
        if not self.__razao_social:
            raise Exception('Razão social é campo obrigatório')
        
        if not self.__cnpj:
            raise Exception('CNPJ é campo obrigatório')
        
        if not self.__detalhes:
            self.__detalhes = ''
        
        if not self.__data_de_emissao:
            self.__data_de_emissao = date.today()
        
        return NotaFiscal(razao_social=self.__razao_social, 
                          cnpj=self.__cnpj, 
                          data_de_emissao=self.__data_de_emissao,
                          detalhes=self.__detalhes, itens=self.__itens)


if __name__ == '__main__':
    gerador = GeradorDeNotaFiscal()
    nota_fiscal = gerador.com_razao_social('Builder SA')\
                         .com_cnpj('07800459000119')\
                         .com_detalhes('Detalhes e mais detalhes')\
                         .com_itens(['item1', 'item2', 'item3'])\
                         .constroi()
                           
    print('Nota Fiscal')
    print(f'Razão social: {nota_fiscal.razao_social}')
    print(f'CNPJ: {nota_fiscal.cnpj}')
    print(f'Data de emissão: {nota_fiscal.data_de_emissao}')
    print(f'Detalhes: {nota_fiscal.detalhes}')
    print(f'Itens: {", ".join(nota_fiscal.itens)}')
