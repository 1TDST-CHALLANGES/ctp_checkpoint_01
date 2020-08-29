import main
import listar
senha_correta = ("yN1825*a")

def alterar_produto():
    cont = 3
    senha = input("Digite sua senha: ")
    while senha != "yN1825*a" and cont > 1:
        print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
        senha = input("Digite novamente.\nSenha: ")
        cont = cont - 1
    if senha == senha_correta:
        print("\033[32mAcesso permitido!\033[m")
        codigo = input("Código: ")
        # verifica se o codigo existe na lista
        if codigo in main.codigo:
            # itera produto por produto em estoque
            for produto in main.estoque:
                # se o produto tiver o codigo digitado
                if produto[0] == codigo:
                    listar.exibir_produto(codigo)
                    novo_desc = input("Digite a nova descrição: ").upper()
                    novo_quant = int(input("Digite a nova quantia: "))
                    produto[1] = novo_desc
                    while novo_quant <= 0:
                        print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
                        novo_quant = int(input("Digite a nova quantia: "))
                    produto[2] = novo_quant
                    print("\n\033[32mAlteração finalizada!\033[m")
                    break
        else:
            print("\033[31mProduto não cadastrado.\033[m")
    else:
        print("\033[31mSeu acesso foi bloqueado! Procure o administrador.\033[m")
        exit()