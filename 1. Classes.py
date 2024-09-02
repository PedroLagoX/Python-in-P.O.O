import os 

os.system("cls || clear")

class Aluno:
    #nome, idade

    def __init__(self, nome: str, idade: int) -> None:
        #Atributos
        self.nome = nome
        self.idade = idade


    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"


# Instanciar classe.

aluno = Aluno("Pedro", 19)

#print(f"Nome: {aluno.nome}")
#print(f"Idade: {aluno.idade}")
print(aluno.exibir_dados())

