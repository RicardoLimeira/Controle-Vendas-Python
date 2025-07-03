import sqlite3

def conectar():
    return sqlite3.connect("data/loja.db")

def criar_tabelas():
    con = conectar()
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    );''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        data_venda TEXT NOT NULL,
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    );''')

    con.commit()
    con.close()
