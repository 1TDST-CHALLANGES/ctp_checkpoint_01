import main

def comprar_produto():
    codigo = int(input("Código do produto: "))
    for alterar in main.estoque:
        if main.estoque[0] == codigo:
            for produto in estoque:
              print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
              print(6 * '-', '', 9 * '-', ' ', 22 * '-')
              print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            quant_prod = int(input("Quanto deseja comprar: "))  # ==> Comprando somente o primeiro item da lista
            while quant_prod <= 0:
                print("\033[31mImpossível comprar uma quantia menor ou igual a zero\033[m")
                quant_prod = int(input("Quanto deseja comprar: "))

            main.estoque[2] = quant_prod + main.estoque[2]
            for produto in estoque:
              print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
              print(6 * '-', '', 9 * '-', ' ', 22 * '-')
              print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            break
        else:
            print("\033[31mProduto não cadastrado\033[m")
            break