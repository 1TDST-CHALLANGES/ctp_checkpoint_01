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
            if produto[0] == codigo:
                if qtd_prod > int(produto[2]): # conversão necessária para a validação
                    print("Quantia digitada é maior que a disponível em estoque.\nDisponibilidade: ", produto[0])
                elif qtd_prod <= 0: # verifica se a quantia digitada é <= a zero
                    print("Quantia digitada é menor ou igual a zero.")
                else:
                    if produto[0] == codigo: # procura o código do produto dentro do estoque
                        listar.exibir_produto(codigo)
                        produto[2] = int(produto[2]) - qtd_prod # realiza a subtração da venda
                        print("\t\tATUALIZAÇÃO: ")
                        listar.exibir_produto(codigo)
    else:
        print("\033[31mProduto não cadastrado\033[m")
    
    

