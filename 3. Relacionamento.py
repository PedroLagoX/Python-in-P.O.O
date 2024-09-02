import os 
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    
class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereco: {self.endereco}"
    


aluno = Aluno("Pedro", 19, Endereco("Rua A", 22))

print(aluno)

