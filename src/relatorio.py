from .database import conectar

def gerar_relatorio():
    con = conectar()
    cur = con.cursor()
    cur.execute('''
        SELECT p.nome, SUM(v.quantidade) AS total_vendido,
               SUM(v.quantidade * p.preco) AS valor_total
        FROM vendas v
        JOIN produtos p ON v.produto_id = p.id
        GROUP BY p.nome;
    ''')
    resultado = cur.fetchall()
    con.close()
    return resultado
