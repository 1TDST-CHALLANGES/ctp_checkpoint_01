import main


def vender_produto():
    codigo = int(input("Código do produto: "))
    for alterar in main.produto:
        if main.produto[0] == codigo:
            for produto in estoque:
                print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
                print(6 * '-', '', 9 * '-', ' ', 22 * '-')
                print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            quant_prod = int(input("Quanto deseja vender: "))
            while quant_prod <= 0:
                print(
                    "\033[31mImpossível vender uma quantia menor ou igual a zero\033[m")  # ==> Vendendo somente o primeiro item da lista

        elif quant_prod > main.estoque:
            quant_prod = int(input("Quanto deseja vender: "))
            main.estoque[2] = main.estoque[2] - quant_prod
            for produto in estoque:
                print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
                print(6 * '-', '', 9 * '-', ' ', 22 * '-')
                print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            break


        else:
            print("\033[31mProduto não cadastrado\033[m")
            break
