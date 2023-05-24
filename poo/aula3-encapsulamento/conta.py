class Conta:
    def __init__(self, numero,  titular, saldo, limite=100):
        self.__numero = numero # em python tornamos um elemento privado com 2 underlines ele esta protegido.com nenhum underline, esta publico
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite # esse atribunto possui um valor padrão de forma o usuario poderá pu nao informa este valor

    def relatorio(self):
        print(f"Olá {self.__titular} o numero da sua conta e {self.__numero} e o seu saldo atual e R${self.__saldo} o seu limite e R$ {self.__limite}")

    def exibirSaldo(self):
        print(f"o seu saldo e {self.__saldo}")
    
    # O metodo get ira retonar ou exibir o valor do atributo
    def getLimite(self):
        return self.__limite
    
    # O metodo set ira alterar o conteudo do atributo, sem exibir nada
    def setLimite(self, valor):
        if valor >0:
            print("Valor menor que zero, informe outro valor")
        else:
            self.__limite = valor

    # VAMOS MODIFICAR ATRIBUNTO SALDO COM @PROPERTY E @SETTER
    @property
    def saldo(self):
        print(f"Ola seu saldo e {self.__saldo}\n")

    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print("Voce não pode inserir valor negativo ou zero\n")
        else:
            self.__saldo = valor