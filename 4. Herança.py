from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float)  -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 # Acréscimo de 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1 # Acréscimo de 20%
        salario_final = self.salario * BONIFICACAO
        return salario_final

#instanciar classes.

#funcionario = Funcionario("Pedro", 10, 10000)
#print(f"Nome: {funcionario1.nome}")

gerente1 = Gerente("Pedro", 20, 2000)
print(f"Nome: {gerente1.nome}")
print(f"Salario: {gerente1.calcular_salario()}")
print("\n")
motoboy1 = Motoboy("Ariel", 22, 2000, "A/B")
print(f"Nome: {motoboy1.nome}")
print(f"Salario: {motoboy1.calcular_salario()}")
