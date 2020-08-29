import main
import listar


def comprar_produto():
    codigo = input("Código do produto: ")

    if codigo in main.codigo:
        listar.exibir_produto(codigo)
        qtd_prod = int(input("Quanto deseja comprar: "))
        for produto in main.estoque:
            if qtd_prod <= 0:
                print("Quantia digitada é menor ou igual a zero.")
            else:
                if produto[0] == codigo:  # procura o código do produto dentro do estoque
                    listar.exibir_produto(codigo)
                    produto[2] = int(produto[2]) + qtd_prod  # realiza a soma da compra
                    print("\t\tATUALIZAÇÃO: ")
                    listar.exibir_produto(codigo)
    else:
        print("\033[31mProduto não cadastrado\033[m")
