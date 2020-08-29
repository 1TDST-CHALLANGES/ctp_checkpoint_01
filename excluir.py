import main

def excluir_produto():
    cont = 3
    senha = input("Digite sua senha: ")
    while senha != "yN1825*a" and cont > 1:
        print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
        senha = input("Digite novamente.\nSenha: ")
        cont = cont - 1
    if senha == "yN1825*a":
        print("\033[32mAcesso permitido!\033[m")
        codigo = input("Código: ")
        if codigo in main.codigo:
            for produto in main.estoque:
                print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
                print(6 * '-', '', 9 * '-', ' ', 22 * '-')
                print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            opcao = input("Deseja excluir o produto? [S/N] ").upper()
            if opcao == "s".upper():
                main.estoque(main.estoque[0])
                print("\033[32mProduto excluido com sucesso\033[m")
            elif opcao == "n".upper():
                print("\033[31mProduto não excluido\033[m")
            else:
                print("\033[31mOpção inválida\033[m")
        else:
            print("\033[31mProduto não cadastrado\033[m")
    else:
        print("\033[31mSeu acesso foi bloqueado! Procure o administrador.\033[m")
        exit()