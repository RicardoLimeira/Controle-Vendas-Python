from datetime import datetime
from .database import conectar

def registrar_venda(produto_id, quantidade):
    con = conectar()
    cur = con.cursor()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (?, ?, ?)", (produto_id, quantidade, data))
    con.commit()
    con.close()
