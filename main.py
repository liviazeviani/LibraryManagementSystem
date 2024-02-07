import sqlite3
import livro


#conectando o banco
def connect():
    con = sqlite3.connect('bancoDeDados.db')
    return con

#função que adiciona livro
def add_book(titulo, autor, editora, genero, qtd_exemplares):
    con = connect()
    con.execute("INSERT INTO livros(titulo, autor, editora, genero, qtd_exemplares)\
                 VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, genero, qtd_exemplares))
    con.commit() #registra mudança
    con.close() #fecha conexão
    

#função que adiciona usuário
def add_user(nome, nacionalidade):
    con = connect()
    con.execute("INSERT INTO usuarios(nome, nacionalidade)\
                 VALUES (?, ?)",(nome, nacionalidade))
    con.commit() 
    con.close() 
    
#função que lista todos os livros cadastrados
def list_books():
    con = connect()
    livros = con.execute("SELECT * FROM livros").fetchall()
    con.close()
        
    print("Livros: ")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Gênero: {livro[3]}")
        print(f"Editora: {livro[4]}")
        print(f"Exemplares: {livro[5]}")
        print("\n")

    if not livros:
        print("Não há livros na biblioteca")

#funcão que realiza empréstimo
def loan(id_livro, data_emprestimo, data_devolucao):
    con = connect()
    con.execute("INSERT INTO emprestimos(id_livro, data_emprestimo, data_devolucao)\
                VALUES(?, ?, ?)", (id_livro, data_emprestimo, data_devolucao))
    con.commit()
    con.close()
    """
     if livro.qtd_exemplares > 0:
        livro.qtd_exemplares -= 1
        print(f'Empréstimo realizado, restam {livro.qtd_exemplares} disponíveis')
    else:
         print(f'Não existem mais exemplares disponíveis')
    """
   

#funcão que exibe lista de livros emprestados
def list_loan():
    con = connect()
    lista_emprestados = con.execute("SELECT livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                                    FROM livros\
                                    INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                                    WHERE emprestimos.data_devolucao IS NULL").fetchall()
    
    con.close()
    return lista_emprestados

    
#testando
#add_book("Sandman", "Neil Gaiman", "Quadrinhos", "Rocco Editora", 2)
#add_user("Lívia Zeviani", "brasileira")
#list_books()
loan(1, "04-02", "04-05")
print(list_loan())
    