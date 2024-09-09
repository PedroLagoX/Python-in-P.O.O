from enum import Enum
import os 
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id:str, nome:str, idade:int, salario:float, setor:Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSalario: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            )
    
funcionario_1 = Funcionario("11", "Pedro", 19, 100000, Setor.FINANCEIRO, Sexo.MASCULINO)
print(funcionario_1)
