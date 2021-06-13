# Chain of Responsibility

O _Chain of Responsibility_ é útil quando diversos objetos de um mesmo tipo precisam ser enfileirados em uma ordem específica, cada um sabendo qual é o próximo a ser chamado. No caso de uma calculadora de descontos, como neste exemplo, um desconto chama o desconto seguinte caso o orçamento recebido não atenda as condições para sua própria aplicação. No fim dessa cadeia, a classe SemDesconto retorna 0 e finaliza o nó, caso nenhum desconto tenha sido aplicado.