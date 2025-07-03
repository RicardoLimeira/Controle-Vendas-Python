from .database import conectar

def adicionar_produto(nome, preco):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
    con.commit()
    con.close()

def listar_produtos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    con.close()
    return produtos
