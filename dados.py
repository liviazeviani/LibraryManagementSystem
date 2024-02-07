import sqlite3

#criando o banco
con = sqlite3.connect('bancoDeDados.db')

#criando tabela de livros

con.execute('CREATE TABLE livros(\
            id INTEGER PRIMARY KEY,\
            titulo TEXT,\
            autor TEXT,\
            editora TEXT,\
            genero TEXT,\
            qtd_exemplares INTEGER)')

#criando tabela de usuários

con.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXT,\
            nacionalidade TEXT)')

#criando tabela de emprestimo

con.execute('CREATE TABLE emprestimos(\
            id INTEGER PRIMARY KEY,\
            id_livro INTEGER,\
            data_emprestimo TEXT,\
            data_devolucao TEXT,\
            estado_livro TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id))')

