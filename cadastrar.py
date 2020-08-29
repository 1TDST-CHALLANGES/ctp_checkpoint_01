import main
import listar


def cadastrar_produto():
    _codigo = input("Código do produto: ")

    if _codigo in main.codigo:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        main.codigo.append(_codigo)
        main.descricao = input("Descrição do produto: ").upper()
        main.quantidade = input("Quantidade de estoque: ")
        main.estoque.append([_codigo, main.descricao, main.quantidade])
        while int(main.quantidade) <= 0:
            print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
            main.quantidade = input("Quantidade de estoque: ")
        print("\n\t\tPRODUTO CADASTRADO\n")
        listar.exibir_produto(_codigo)
