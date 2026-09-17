class Livro:
    def __init__(self, titulo, autor, paginas):
        """Método construtor para inicializar os atributos do livro."""
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        """Método especial para retornar a representação em texto do objeto."""
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"


def executar_sistema():
    print("--- Cadastro de Livro - Biblioteca Digital ---")
    
    # Solicita os dados ao usuário
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    
    # Tratamento simples para garantir que as páginas sejam um número inteiro
    try:
        paginas = int(input("Digite a quantidade de páginas: "))
    except ValueError:
        print("Erro: A quantidade de páginas deve ser um número. Definido como 0.")
        paginas = 0

    # Cria a instância (objeto) da classe Livro
    novo_livro = Livro(titulo, autor, paginas)

    # Exibe a descrição formatada usando o método __str__
    print("\n--- Conferência de Dados ---")
    print(novo_livro)


# Executa o programa
if __name__ == "__main__":
    executar_sistema()
