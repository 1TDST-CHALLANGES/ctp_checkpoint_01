global senha_correta
global codigo
global descricao
global quantidade
global estoque

senha_correta = ("yN1825*a")
codigo = []
descricao = []
quantidade = []
estoque = []

def cadastrar():
    _codigo = input("Código do produto: ")
    if _codigo in codigo:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        codigo.append(_codigo)
        descricao = input("Descrição do produto: ").upper()
        _quantidade = int(input("Quantidade de estoque: "))
        while int(_quantidade) <= 0:
            print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
            _quantidade = int(input("Quantidade de estoque: "))
        quantidade.append(_quantidade)
        estoque.append([_codigo, descricao, _quantidade])
        print("\033[32m\n\t\tPRODUTO CADASTRADO\n\033[m")
        exibir_produto(_codigo)

def alterar():
    cont = 3
    senha = input("Digite sua senha: ")
    while senha != "yN1825*a" and cont > 1:
        print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
        senha = input("Digite novamente.\nSenha: ")
        cont = cont - 1
    if senha == senha_correta:
        print("\033[32mAcesso permitido!\033[m")
        codigo = input("Código: ")
        if codigo in codigo:
            for produto in estoque:
                if produto[0] == codigo:
                    exibir_produto(codigo)
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

def excluir():
    cont = 3
    senha = input("Digite sua senha: ")
    while senha != "yN1825*a" and cont > 1:
        print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
        senha = input("Digite novamente.\nSenha: ")
        cont = cont - 1
    if senha == senha_correta:
        print("\033[32mAcesso permitido!\033[m")
        codigo = input("Código: ")
        if codigo in codigo:
            for produto in estoque:
                if produto[0] == codigo:
                    exibir_produto(codigo)
                    opcao = input("Deseja excluir o produto? [S/N] ").upper()
                    if opcao == "s".upper():
                        estoque.remove(produto)
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

def exibir_produto(codigo):
    for produto in estoque:
        if produto[0] == codigo:
            print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')
            print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')

def listar_produtos():
    qtd_cadastrados=0
    qtd_estoque=0
    print("\nCÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
    print(6 * '-', '', 9 * '-', ' ', 22 * '-')
    for produto in estoque:
      if int(produto[2]) < 100:
        qtd_estoque+=1
        qtd_cadastrados+=1
        print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
      else:
        print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
        qtd_cadastrados+=1
    print(6 * '-', '', 9 * '-', ' ', 22 * '-')
    print("\nTotal de produtos cadastrados: ", qtd_cadastrados)
    print("Quantidade de itens em estoque: ", sum(quantidade))
    print("Produto com estoque abaixo do mínimo permitido (100 unidades): ", qtd_estoque)

def comprar():
    codigo = input("Código do produto: ")
    if codigo in codigo:
        exibir_produto(codigo)
        qtd_prod = int(input("Quanto deseja comprar: "))
        for produto in estoque:
            if qtd_prod <= 0:
                print("Quantia digitada é menor ou igual a zero.")
            else:
                if produto[0] == codigo:
                    exibir_produto(codigo)
                    produto[2] = int(produto[2]) + qtd_prod
                    print("\033[32m\t\tATUALIZAÇÃO: \033[m")
                    exibir_produto(codigo)
    else:
        print("\033[31mProduto não cadastrado\033[m")

def vender():
    codigo = input("Código do produto: ")
    if codigo in codigo:
        exibir_produto(codigo)
        qtd_prod = int(input("Quanto deseja vender: "))
        for produto in estoque:
            if produto[0] == codigo:
                if qtd_prod > int(produto[2]):
                    print("\033[31mQuantia digitada é maior que a disponível em estoque.\n\033[mDisponibilidade: ",
                          produto[2])
                elif qtd_prod <= 0:
                    print("\033[31mQuantia digitada é menor ou igual a zero.\033[m")
                else:
                    if produto[0] == codigo:
                        exibir_produto(codigo)
                        produto[2] = int(produto[2]) - qtd_prod
                        print("\033[32m\n\t\tATUALIZAÇÃO: \033[m\n")
                        exibir_produto(codigo)
    else:
        print("\033[31mProduto não cadastrado\033[m")

