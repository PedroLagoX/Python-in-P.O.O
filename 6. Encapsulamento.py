import os

os.system("cls || clear")

#Criando sua própria exceção.
class SaldoInsuficienteError(Exception):
    pass

#Criando sua própria exceção.
class ValorNegativoError(Exception):
    pass


class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #Atributo protegido

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor) -> float:
        #try - expect
        try:
            self.__verificar_sacar(valor) #Método privado.
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"

        self.verificar_sacar(valor)
        self._saldo -= valor
        return self._saldo

    def __verificar_sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.") #Lançando um erro.
    
    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as erro:
            return f"Erro: {erro}"

        self._saldo += valor
        return self._saldo

    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Não é possivel depositar valor negativo")


class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar classes.
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaCorrente(444, 555)

# print(conta_corrente._saldo)
# conta_corrente._saldo += 200

print(conta_corrente.saldo)

print(conta_corrente.sacar(200))

print(conta_corrente.saldo)

print(conta_corrente.depositar(-200))