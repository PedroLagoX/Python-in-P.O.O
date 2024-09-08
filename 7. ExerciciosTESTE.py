from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade:str) -> None:
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
    def __init__(self, nome:str, email:str, salario:float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalário: {self.salario}"
                f"\nEndereço {self.endereco}"
                )
    
class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, cnh:str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)


motoboy = Motoboy("Ariel", "ariel157@gmail.com", 1000, "AB", Endereco("Rodão", "88", "Salvador"))
print(motoboy)
print("\n==========|==========")
gerente = Gerente("Pedro", "pedrolago@gmail.com", 10000, Endereco("Rodão", "8", "Salvador"))
print(gerente)