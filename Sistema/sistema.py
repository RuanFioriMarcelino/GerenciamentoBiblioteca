import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='biblioteca',
    user='root',
    password='9872',
    )

if conexao.is_connected():
    db_info = conexao.get_server_info()
    print("Conexão bem sucedida",db_info)
    cursor = conexao.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)



janela = ctk.CTk()

class programa():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.usuario_entry = None
        self.senha_entry = None
        self.titulo= None
        self.ano = None
        self.genero = None
        self.preco = None
        self.quantidade = None
        self.font_btn = ctk.CTkFont(size=18, family="Arial", weight="bold")
        self.tela_login() 
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Gerenciamento de Biblioteca")
        janela.iconbitmap("icon.ico")
        janela.resizable(False, False)

    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        usuario1 = "1"
        senha1 = "1"

        if usuario == '' or senha == '':
            messagebox.showerror(title="Login", message="Por favor, preencha todos os campos!")
        else:
            if usuario != usuario1:
                messagebox.showerror(title="Login", message="Usuário não encontrado no sistema.")
            elif senha != senha1:
                messagebox.showerror(title="Login", message="Senha incorreta.")
            else:
                messagebox.showinfo(title="Login", message="Login feito com sucesso!")
                self.fechar_login()

    def tela_login(self):
        label_biblioteca = ctk.CTkLabel(master=janela, text='Biblioteca da Info', font=('Roboto', 24, 'bold'), text_color='white')
        label_biblioteca.place(x=60, y=20)

        img = PhotoImage(file="logo.png")
        label_img = ctk.CTkLabel(master=janela, text="", image=img)
        label_img.place(x=80, y=60)

        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=ctk.RIGHT)

        label_login = ctk.CTkLabel(master=login_frame, text='Faça o Login', font=('Roboto', 24, 'bold'), text_color='white')
        label_login.place(x=35, y=20)

        self.usuario_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
        self.usuario_entry.place(x=25, y=105)
        ctk.CTkLabel(master=login_frame, text="Campo obrigatório.", text_color="green", font=("Roboto", 10)).place(x=25, y=135)

        self.senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de usuário", width=300, font=("Roboto", 14), show="*")
        self.senha_entry.place(x=25, y=175)
        ctk.CTkLabel(master=login_frame, text="Campo obrigatório.", text_color="green", font=("Roboto", 10)).place(x=25, y=205)

        ctk.CTkCheckBox(master=login_frame, text="Lembrar de mim").place(x=25, y=235)

        ctk.CTkButton(master=login_frame, text="login", width=300, command=self.login).place(x=25, y=285)


    def fechar_login(self):
        self.usuario_entry.delete(0, 'end')
        self.senha_entry.delete(0, 'end')
        for i in self.janela.winfo_children(): 
            i.destroy()
        self.tela_opcao()

    def voltar(self):
        for i in self.janela.winfo_children(): 
            i.destroy()
        self.tela_opcao()
    
    def limpar_tela(self):
        for i in self.janela.winfo_children(): 
            i.destroy()


    def insert_livro(self):
        quantidade = int(self.quantidade.get())
        preco = float(self.preco.get())

        comando = f'INSERT INTO livros (titulo,ano,genero,preco,quantidade) VALUES ("{self.titulo.get()}", "{self.ano.get()}","{self.genero.get()}", {preco}, {quantidade})'
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()

        self.titulo.delete(0, 'end')
        self.ano.delete(0, 'end')
        self.genero.delete(0, 'end')
        self.preco.delete(0, 'end')
        self.quantidade.delete(0, 'end')

    
    def cad_livro(self):
        self.opcao_frame.destroy()

        cad_livro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cad_livro_frame.pack(side=ctk.RIGHT)
        
        texto = ctk.CTkLabel(cad_livro_frame, text="Cadastrar Livro", font=('Roboto', 24, 'bold'))
        texto.place(x=80, y=20)

        self.titulo = ctk.CTkEntry(cad_livro_frame, placeholder_text="Título", height=35, width=304)
        self.titulo.place(x=25, y=70)

        self.ano = ctk.CTkEntry(cad_livro_frame, placeholder_text="Ano", height=35, width=304)
        self.ano.place(x=25, y=115)

        self.genero = ctk.CTkEntry(cad_livro_frame, placeholder_text="Gênero", height=35, width=304)
        self.genero.place(x=25, y=160)

        self.preco = ctk.CTkEntry(cad_livro_frame, placeholder_text="Preço", height=35, width=304)
        self.preco.place(x=25, y=205)

        self.quantidade = ctk.CTkEntry(cad_livro_frame, placeholder_text="Quantidade", height=35, width=304)
        self.quantidade.place(x=25, y=250)

        btn_enviar = ctk.CTkButton(cad_livro_frame, text="Cadastrar", font=self.font_btn, command=self.insert_livro, height=35, width=304)
        btn_enviar.place(x=25, y=295)

        btn_voltar = ctk.CTkButton(cad_livro_frame, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=25, y=340)

    def insert_cliente(self):
        cpf = int(self.cpf.get())
        comando = f'INSERT INTO clientes (nome, cpf, endereco) VALUES ("{self.nome.get()}", {cpf}, "{self.endereco.get()}")'
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        self.nome.delete(0, 'end')
        self.cpf.delete(0, 'end')
        self.endereco.delete(0, 'end')


    def cad_cliente(self):
        self.opcao_frame.destroy()

        cadCliente_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cadCliente_frame.pack(side=ctk.RIGHT)
        
        texto = ctk.CTkLabel(cadCliente_frame, text="Cadastrar Cliente",  font=('Roboto', 24, 'bold'))
        texto.place(x=80, y=40)

        self.nome = ctk.CTkEntry(cadCliente_frame, placeholder_text="Nome", height=35, width=304)
        self.nome.place(x=25, y=130)

        self.cpf = ctk.CTkEntry(cadCliente_frame, placeholder_text="CPF", height=35, width=304)
        self.cpf.place(x=25, y=180)

        self.endereco = ctk.CTkEntry(cadCliente_frame, placeholder_text="Endereco", height=35, width=304)
        self.endereco.place(x=25, y=230)
        
        btn_enviar = ctk.CTkButton(cadCliente_frame, text="Cadastrar", font=self.font_btn, command=self.insert_cliente, height=35, width=304)
        btn_enviar.place(x=25, y=280)

        btn_voltar = ctk.CTkButton(cadCliente_frame, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=25, y=330)

    def verlivro(self):
        self.opcao_frame.destroy()
        self.limpar_tela()

        cursor.execute("SELECT * FROM livros")
        tabela = cursor.fetchall()
        
        ver_livros = ctk.CTkFrame(master=janela, width=690, height=340)
        ver_livros.pack()

        cabecario = ["ID", "Título", "Ano", "Gênero", "Preço", "Quantidade"]
        for i, coluna in enumerate(cabecario):
            ctk.CTkLabel(ver_livros, text=coluna, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=30, pady=5)

        for i, linha in enumerate(tabela, start=1):
            for coluna, col_value in enumerate(linha):
                ctk.CTkLabel(ver_livros, text=str(col_value)).grid(row=i, column=coluna, padx=30, pady=5)

        btn_voltar = ctk.CTkButton(master=janela, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=200, y=355)

    def vercliente(self):
        self.opcao_frame.destroy()
        self.limpar_tela()

        cursor.execute("SELECT * FROM clientes")
        tabela = cursor.fetchall()
        
        ver_livros = ctk.CTkFrame(master=janela, width=690, height=340)
        ver_livros.pack()

        cabecario = ["ID", "Nome", "CPF", "Endereço"]
        for i, coluna in enumerate(cabecario):
            ctk.CTkLabel(ver_livros, text=coluna, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=30, pady=5)

        for i, linha in enumerate(tabela, start=1):
            for coluna, col_value in enumerate(linha):
                ctk.CTkLabel(ver_livros, text=str(col_value)).grid(row=i, column=coluna, padx=30, pady=5)

        btn_voltar = ctk.CTkButton(master=janela, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=200, y=355)

    def veremprestimos(self):
        self.opcao_frame.destroy()
        self.limpar_tela()
        
        cursor.execute("""Select emprestimos.id, emprestimos.dataemprestimo, emprestimos.datadevolucao, clientes.nome, livros.id
                            from emprestimos, clientes, livros
                            where emprestimos.idcliente = clientes.id
                            and	emprestimos.idlivro = livros.id""")
        tabela = cursor.fetchall()
        
        ver_livros = ctk.CTkFrame(master=janela, width=690, height=340)
        ver_livros.pack()

        cabecario = ["ID", "Data do Empréstimo", "Data da Devolução", "Nome", "ID do Livro"]
        for i, coluna in enumerate(cabecario):
            ctk.CTkLabel(ver_livros, text=coluna, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=30, pady=5)

        for i, linha in enumerate(tabela, start=1):
            for coluna, dados in enumerate(linha):
                ctk.CTkLabel(ver_livros, text=str(dados)).grid(row=i, column=coluna, padx=30, pady=5)

        btn_voltar = ctk.CTkButton(master=janela, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=200, y=355)



    def insert_emprestimo(self):
        idcliente = int(self.idcliente.get())
        idlivro = int(self.idlivro.get())

        comando = f'INSERT INTO emprestimos (dataemprestimo, datadevolucao, idlivro, idcliente) VALUES ("{self.dataemprestimo.get()}", "{self.datadevolucao.get()}", {idlivro}, {idcliente})'
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        self.dataemprestimo.delete(0, 'end')
        self.datadevolucao.delete(0, 'end')
        self.idlivro.delete(0, 'end')
        self.idcliente.delete(0, 'end')

    def cad_emprestimo(self):
        self.opcao_frame.destroy()

        cad_emprestimo = ctk.CTkFrame(master=janela, width=350, height=396)
        cad_emprestimo.pack(side=ctk.RIGHT)

        texto = ctk.CTkLabel(cad_emprestimo, text="Cadastrar empréstimo",  font=('Roboto', 24, 'bold'))
        texto.place(x=45, y=30)

        self.idcliente = ctk.CTkEntry(cad_emprestimo, placeholder_text="ID do cliente", height=35, width=304)
        self.idcliente.place(x=25, y=80)

        self.idlivro = ctk.CTkEntry(cad_emprestimo, placeholder_text="ID do Livro", height=35, width=304)
        self.idlivro.place(x=25, y=130)

        self.dataemprestimo = ctk.CTkEntry(cad_emprestimo, placeholder_text="Data do empréstimo", height=35, width=304)
        self.dataemprestimo.place(x=25, y=180)

        self.datadevolucao = ctk.CTkEntry(cad_emprestimo, placeholder_text="Data de devoluçao", height=35, width=304)
        self.datadevolucao.place(x=25, y=230)
        
        btn_enviar = ctk.CTkButton(cad_emprestimo, text="Cadastrar", font=self.font_btn, command=self.insert_emprestimo, height=35, width=304)
        btn_enviar.place(x=25, y=280)

        btn_voltar = ctk.CTkButton(cad_emprestimo, text="Voltar", font=self.font_btn, command=self.voltar, height=35, width=304)
        btn_voltar.place(x=25, y=330)

    def tela_opcao(self):
        img = PhotoImage(file="logo.png")
        label_img = ctk.CTkLabel(master=janela, text="", image=img)
        label_img.place(x=80, y=60)

        self.opcao_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        self.opcao_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=self.opcao_frame, text='Escolha o que deseja fazer', font=('Roboto', 24, 'bold'), text_color='white')
        label.place(x=25, y=20)

        btn_livro = ctk.CTkButton(self.opcao_frame, text="Cadastrar Livro", command=self.cad_livro, font=self.font_btn, height=35, width=304)
        btn_livro.place(x=25, y=80)

        btn_cliente = ctk.CTkButton(self.opcao_frame, text="Cadastrar Cliente", command=self.cad_cliente, font=self.font_btn, height=35, width=304)
        btn_cliente.place(x=25, y=130)

        btn_verLivro = ctk.CTkButton(self.opcao_frame, text="Ver Livros", font=self.font_btn, command=self.verlivro, height=35, width=304)
        btn_verLivro.place(x=25, y=180)

        btn_vercliente = ctk.CTkButton(self.opcao_frame, text="Ver Clientes", font=self.font_btn, command=self.vercliente, height=35, width=304)
        btn_vercliente.place(x=25, y=230)

        btn_emprestimo = ctk.CTkButton(self.opcao_frame, text="Cadastrar Emprestimo", font=self.font_btn, command=self.cad_emprestimo, height=35, width=304)
        btn_emprestimo.place(x=25, y=280)

        btn_verEmprestimo = ctk.CTkButton(self.opcao_frame, text="Ver Emprestimos", font=self.font_btn,command=self.veremprestimos, height=35, width=304)
        btn_verEmprestimo.place(x=25, y=330)

programa()

if conexao.is_connected():
    cursor.close()
    conexao.close()
    print("Conexão ao MySQL encerrada")