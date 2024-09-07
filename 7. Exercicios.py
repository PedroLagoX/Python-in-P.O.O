from abc import ABC, abstractmethod
import os 
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nCidade: {self.cidade}"
            )

class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = Endereco

    @classmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nEmail: {self.email}"
            f"\nSalario: {self.salario}"
            f"\nEndereço: {self.endereco}"
        )

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def salario_final(self) -> float:
        return 1000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nSalario: {self.salario_final()}")

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)

    def salario_final(self) -> float:
        return 2000.0

motoboy = Motoboy("Zeca", "carol123@gmail.com", 1000, "A", Endereco("AvB", "16", "SSA"))

print(motoboy)

gerente = Gerente("Pedro", "pedro375@gmail.com", 2000,
                  Endereco("Rodão", "8", "Salvador"))
print(gerente)
