from src.database import criar_tabelas
from src.produtos import adicionar_produto, listar_produtos
from src.vendas import registrar_venda
from src.relatorio import gerar_relatorio

def menu():
    while True:
        print("\n=== CONTROLE DE VENDAS ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Registrar Venda")
        print("4. Relatório de Vendas")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            adicionar_produto(nome, preco)

        elif op == "2":
            produtos = listar_produtos()
            for p in produtos:
                print(f"{p[0]} - {p[1]} - R${p[2]:.2f}")

        elif op == "3":
            listar = listar_produtos()
            for p in listar:
                print(f"{p[0]} - {p[1]} - R${p[2]:.2f}")
            produto_id = int(input("ID do produto: "))
            qtd = int(input("Quantidade: "))
            registrar_venda(produto_id, qtd)

        elif op == "4":
            relatorio = gerar_relatorio()
            for r in relatorio:
                print(f"{r[0]} | Quantidade: {r[1]} | Faturamento: R${r[2]:.2f}")

        elif op == "0":
            break

if __name__ == "__main__":
    criar_tabelas()
    menu()
