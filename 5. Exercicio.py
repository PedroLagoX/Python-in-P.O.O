from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"    
            )

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    @classmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}"
                )
    
class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nSalario: {self.salario_final()}")
    
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0

#Instanciando classes.
print("\n=== Dados do engenheiro ===")
engenheiro_1 = Engenheiro("Pedro", "719865", "pedro@gmail.com", "SIM",
                          Endereco("Rua A", "8", "3", "40355", "Salvador"))
print(engenheiro_1)

print("\n=== Dados do medico ===")
medico_1 = Engenheiro("Helena", "714456", "lhelena@gmail.com", "SIM",
                          Endereco("Rua B", "5", "2", "40500", "Salvador"))
print(medico_1)