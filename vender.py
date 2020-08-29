import main
import listar

def vender_produto():
    codigo = input("Código do produto: ")

    # verifica se o código digitado já está na lista codigo (inserida em estoque)
    if codigo in main.codigo:
        listar.exibir_produto(codigo)
        qtd_prod = int(input("Quanto deseja vender: "))
        # irá percorrer produto por produto em estoque
        for produto in main.estoque:
            if qtd_prod > int(produto[2]): #conversão necessária para a validação
                print("Quantia digitada é maior que", produto[2],"(disponível em estoque.)")
            elif qtd_prod <= 0:
                print("Quantia digitada é menor ou igual a zero.")
            else:
                if produto[0] == codigo:
                    listar.exibir_produto(codigo)
                    produto[2] = int(produto[2]) - qtd_prod
                    print("\t\tATUALIZAÇÃO: ")
                    listar.exibir_produto(codigo)
    else:
        print("\033[31mProduto não cadastrado\033[m")
    
    

