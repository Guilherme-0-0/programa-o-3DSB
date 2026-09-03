import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


NOME_BANCO = "clientes.db"


def criar_tabela():
    """Cria o banco e a tabela caso ainda não existam."""
    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
            """
        )


def limpar_formulario():
    """Apaga o conteúdo dos campos e posiciona o cursor no nome."""
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()


def salvar_cliente():
    """Valida os campos e salva um cliente no banco de dados."""
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Campos obrigatórios",
            "Preencha o nome, o e-mail e o telefone antes de salvar.",
        )
        return

    try:
        with sqlite3.connect(NOME_BANCO) as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone),
            )

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Não foi possível salvar o cliente:\n{erro}")


def visualizar_clientes():
    """Abre uma nova janela e mostra todos os clientes cadastrados."""
    try:
        with sqlite3.connect(NOME_BANCO) as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, nome, email, telefone FROM clientes ORDER BY id"
            )
            clientes = cursor.fetchall()
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Não foi possível consultar os clientes:\n{erro}")
        return

    janela_clientes = tk.Toplevel()
    janela_clientes.title("Clientes cadastrados")
    janela_clientes.geometry("720x360")

    titulo = tk.Label(
        janela_clientes,
        text="Clientes cadastrados",
        font=("Arial", 16, "bold"),
    )
    titulo.pack(pady=(15, 10))

    area_tabela = tk.Frame(janela_clientes)
    area_tabela.pack(padx=15, pady=(0, 15), fill="both", expand=True)

    colunas = ("id", "nome", "email", "telefone")
    tabela = ttk.Treeview(area_tabela, columns=colunas, show="headings")

    tabela.heading("id", text="ID")
    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="E-mail")
    tabela.heading("telefone", text="Telefone")

    tabela.column("id", width=50, anchor="center")
    tabela.column("nome", width=190)
    tabela.column("email", width=260)
    tabela.column("telefone", width=150, anchor="center")

    barra_vertical = ttk.Scrollbar(
        area_tabela, orient="vertical", command=tabela.yview
    )
    tabela.configure(yscrollcommand=barra_vertical.set)

    tabela.pack(side="left", fill="both", expand=True)
    barra_vertical.pack(side="right", fill="y")

    for cliente in clientes:
        tabela.insert("", tk.END, values=cliente)

    if not clientes:
        tabela.insert("", tk.END, values=("-", "Nenhum cliente cadastrado", "-", "-"))


def criar_interface():
    global entrada_nome, entrada_email, entrada_telefone

    janela = tk.Tk()
    janela.title("Cadastro de Clientes")
    janela.geometry("510x290")
    janela.resizable(False, False)

    titulo = tk.Label(
        janela,
        text="Cadastro de Clientes",
        font=("Arial", 18, "bold"),
    )
    titulo.pack(pady=(18, 12))

    formulario = tk.Frame(janela)
    formulario.pack(padx=25, fill="x")

    tk.Label(formulario, text="Nome:", font=("Arial", 11)).grid(
        row=0, column=0, sticky="w", pady=6
    )
    entrada_nome = tk.Entry(formulario, width=35, font=("Arial", 11))
    entrada_nome.grid(row=0, column=1, padx=10, pady=6)

    tk.Label(formulario, text="E-mail:", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", pady=6
    )
    entrada_email = tk.Entry(formulario, width=35, font=("Arial", 11))
    entrada_email.grid(row=1, column=1, padx=10, pady=6)

    tk.Label(formulario, text="Telefone:", font=("Arial", 11)).grid(
        row=2, column=0, sticky="w", pady=6
    )
    entrada_telefone = tk.Entry(formulario, width=35, font=("Arial", 11))
    entrada_telefone.grid(row=2, column=1, padx=10, pady=6)

    botoes = tk.Frame(janela)
    botoes.pack(pady=20)

    botao_salvar = tk.Button(
        botoes,
        text="Salvar",
        width=12,
        bg="#2e7d32",
        fg="white",
        font=("Arial", 10, "bold"),
        command=salvar_cliente,
    )
    botao_salvar.grid(row=0, column=0, padx=8)

    botao_limpar = tk.Button(
        botoes,
        text="Limpar",
        width=12,
        font=("Arial", 10, "bold"),
        command=limpar_formulario,
    )
    botao_limpar.grid(row=0, column=1, padx=8)

    botao_visualizar = tk.Button(
        botoes,
        text="Visualizar Clientes",
        width=18,
        bg="#1565c0",
        fg="white",
        font=("Arial", 10, "bold"),
        command=visualizar_clientes,
    )
    botao_visualizar.grid(row=0, column=2, padx=8)

    entrada_nome.focus()
    janela.mainloop()


if __name__ == "__main__":
    criar_tabela()
    criar_interface()
