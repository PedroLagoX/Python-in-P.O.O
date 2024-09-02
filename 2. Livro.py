import os
os.system("cls || clear")

class Livro:

    def __init__(self, titulo: str, autor: str, numeroPaginas: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numeroPaginas = numeroPaginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nNúmero de Paginas: {self.numeroPaginas} \nPreço: {self.preco}"
    

livro1 = Livro("O Pequeno Principe", "Flavio Pascal", 100, 50)
livro2 = Livro("O Grande Homem", "Pedro Coelho", 150, 25)

print(livro1.exibir_dados())
print("\n")
print(livro2.exibir_dados())