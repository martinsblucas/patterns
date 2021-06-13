# State

O _State_ é um design pattern útil para abstrair, em classes especializadas, os comportamentos de uma classe que variam de acordo com seu estado atual. No exemplo de um orçamento que pode estar em aprovação, aprovado, reprovado e finalizado, delegamos as implementações de troca de estado e aplicação de descontos especiais às classes que representam os possíveis estados.