import main


def cadastro_produto():
    codigo = int(input("Código do produto: "))
    if codigo in main.estoque:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        descricao = input("Descrição do produto: ").upper()
        quantidade = int(input("Quantidade de estoque: "))
        main.estoque.append(codigo)
        main.estoque.append(descricao)
        while quantidade <= 0:
            print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
            quantidade = int(input("Quantidade de estoque: "))

        main.estoque.append(quantidade)

