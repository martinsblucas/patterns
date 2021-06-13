from datetime import date
from abc import ABC, abstractmethod


class Situacao(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def iniciar(self, contrato: 'Contrato'):
        pass
    
    @abstractmethod
    def acertar(self, contrato: 'Contrato'):
        pass
    
    @abstractmethod
    def concluir(self, contrato: 'Contrato'):
        pass


class Novo(Situacao):
    def __str__(self) -> str:
        return 'Novo'
    
    def iniciar(self, contrato: 'Contrato'):
        contrato.situacao = EmAndamento()
    
    def acertar(self, contrato: 'Contrato'):
        raise('Um novo contrato não pode ser acertado')
    
    def concluir(self, contrato: 'Contrato'):
        raise('Um novo contrato não pode ser concluído')


class EmAndamento(Situacao):
    def __str__(self) -> str:
        return 'Em Andamento'
    
    def iniciar(self, contrato: 'Contrato'):
        raise('Um contato em andamento não pode ser iniciado')
    
    def acertar(self, contrato: 'Contrato'):
        contrato.situacao = Acertado()
    
    def concluir(self, contrato: 'Contrato'):
        raise('Um contato em andamento não pode ser concluído')


class Acertado(Situacao):
    def __str__(self) -> str:
        return 'Acertado'
    
    def iniciar(self, contrato: 'Contrato'):
        raise('Um contato acertado não pode ser iniciado')
    
    def acertar(self, contrato: 'Contrato'):
        raise('Um contato acertado não pode ser acertado')
    
    def concluir(self, contrato: 'Contrato'):
        contrato.situacao = Concluido()


class Concluido(Situacao):
    def __str__(self) -> str:
        return 'Concluído'
    
    def iniciar(self, contrato: 'Contrato'):
        raise('Um contato concluído não pode ser iniciado')
    
    def acertar(self, contrato: 'Contrato'):
        raise('Um contrato concluído não pode ser acertado')
    
    def concluir(self, contrato: 'Contrato'):
        raise('Um contrato concluído não pode ser concluído')
    
    
class Estado:
    def __init__(self, contrato: 'Contrato'):
        self.__contrato = contrato
        
    @property
    def contrato(self) -> 'Contrato':
        return self.__contrato


class Contrato:
    def __init__(self, titular, termos = [], data=date.today(), situacao: Situacao = Novo()):
        self.__titular = titular
        self.__termos = termos
        self.__data = data
        self.__situacao = situacao
        
    def obter_estado(self):
        return Estado(Contrato(titular=self.titular, 
                               termos=self.termos,
                               data=self.data,
                               situacao=self.situacao))
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def data(self):
        return self.__data
    
    @property
    def termos(self):
        return self.__termos[:]
    
    @property
    def situacao(self):
        return self.__situacao
    
    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao
        
    def restaurar(self, estado: Estado):
        self.__titular = estado.contrato.titular
        self.__data = estado.contrato.data
        self.__situacao = estado.contrato.situacao
        self.__termos = estado.contrato.termos
    
    def adicionar_termo(self, termo):
        self.__termos.append(termo)

    def iniciar(self):
        self.situacao.iniciar(self)
    
    def acertar(self):
        self.situacao.acertar(self)
    
    def concluir(self):
        self.situacao.concluir(self)
        
    def imprimir_termos(self):
        for i, termo in enumerate(self.termos, start=1):
            print(f'{i}) {termo}')


class Historico:
    def __init__(self):
        self.__estados = []

    def adicionar(self, estado: Estado):
        self.__estados.append(estado)
        
    def obter_pelo_indice(self, indice) -> Estado:
        try:
            return self.__estados[indice]
        except IndexError:
            raise(f'Não há um estado disponível no índice #{indice}')


if __name__ == '__main__':
    historico = Historico()
    
    contrato = Contrato(titular='Titular do contrato',
                        termos=['Termo 1', 'Termo 2', 'Termo 3'])
    
    historico.adicionar(contrato.obter_estado())
    
    contrato.iniciar()
    contrato.adicionar_termo('Termo 4')
    historico.adicionar(contrato.obter_estado())

    print()
    print('Estado atual do contrato')
    print(f'Situação: {contrato.situacao}')
    print('Termos: ')
    contrato.imprimir_termos()
    print()
    
    estado_inicial = historico.obter_pelo_indice(0)
    contrato.restaurar(estado_inicial)
    
    print()
    print('Contrato restaurado a versão inicial')
    print(f'Situação: {contrato.situacao}')
    print('Termos: ')
    contrato.imprimir_termos()
    print()
