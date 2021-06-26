from abc import ABC, abstractmethod
from datetime import date


class Pedido:
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_de_finalizacao = None
        
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def status(self):
        return self.__status
    
    def data_de_finalizacao(self):
        return self.__data_de_finalizacao
    
    def pagar(self):
        self.__status = 'PAGO'
        
    def finalizar(self):
        self.__status = 'ENTREGUE'
        self.__data_de_finalizacao = date.today()


class Comando:
    @abstractmethod
    def executar(self):
        pass
    

class FinalizarPedido(Comando):
    def __init__(self, pedido: Pedido):
        self.__pedido = pedido
        
    def executar(self):
        self.__pedido.finalizar()
        

class PagarPedido(Comando):
    def __init__(self, pedido: Pedido):
        self.__pedido = pedido
        
    def executar(self):
        self.__pedido.pagar()
    
    
class FilaDeTrabalho:
    def __init__(self):
        self.__comandos = []
        
    def adiciona(self, comando: Comando):
        self.__comandos.append(comando)
        
    def processar(self):
        for comando in self.__comandos:
            comando.executar()
            
            
if __name__ == '__main__':
    pedido1 = Pedido('Cliente1', 150)
    pedido2 = Pedido('Cliente 2', 200)
    pedido3 = Pedido('Cliente 3', 400)
    
    fila_de_trabalho = FilaDeTrabalho()
    pagar_pedido1 = PagarPedido(pedido1)
    pagar_pedido3 = PagarPedido(pedido3)
    finalizar_pedido3 = FinalizarPedido(pedido3)
    pagar_pedido2 = PagarPedido(pedido2)
    finalizar_pedido1 = FinalizarPedido(pedido1)
    finalizar_pedido2 = FinalizarPedido(pedido2)
    
    fila_de_trabalho.adiciona(pagar_pedido1)
    fila_de_trabalho.adiciona(pagar_pedido3)
    fila_de_trabalho.adiciona(finalizar_pedido3)
    fila_de_trabalho.adiciona(pagar_pedido2)
    fila_de_trabalho.adiciona(finalizar_pedido1)
    fila_de_trabalho.adiciona(finalizar_pedido2)
    
    print('Antes de processar a fila')
    print(f'Status do pedido 1: {pedido1.status}')
    print(f'Status do pedido 2: {pedido2.status}')
    print(f'Status do pedido 3: {pedido3.status}')
    
    fila_de_trabalho.processar()
    
    print('Depois de processar a fila')
    print(f'Status do pedido 1: {pedido1.status}')
    print(f'Status do pedido 2: {pedido2.status}')
    print(f'Status do pedido 3: {pedido3.status}')
