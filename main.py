import cadastrar
import alterar
import excluir
import comprar
import vender
import listar

menu = 0

codigo = []
descricao = []
quantidade = []
estoque = []

# TODO: utilizar tupla
# TODO: opcao de voltar no menu
# TODO: importar funcao cadastrar_produto (problema de import)

while menu != 7:
    print("\nMenu")
    opcao = int(input(
        "\t1 - Cadastrar Produto\n\t2 - Alterar Produto\n\t3 - Excluir Produto""\n\t4 - Listar Estoque\n\t5 - Comprar "
        "Produto""\n\t6 - Vender Produto\n\t7 - Sair\n\nDigite a opção desejada: "))
    if opcao == 1:  # Cadastrar Produto
        #cadastrar_produto()
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            _codigo = input("Código do produto: ")

            if _codigo in codigo:
                print("\033[31mCódigo já cadastrado\033[m")
            else:
                codigo.append(_codigo)
                descricao = input("Descrição do produto: ").upper()
                _quantidade = input("Quantidade de estoque: ")
                while int(_quantidade) <= 0:
                    print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
                    _quantidade = input("Quantidade de estoque: ")
                quantidade.append(_quantidade)
                estoque.append([_codigo, descricao, _quantidade])
                print("\033[32m\n\t\tPRODUTO CADASTRADO\n\033[m")
                listar.exibir_produto(_codigo)
                break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    elif opcao == 2:  # Alterar Produto
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            alterar.alterar_produto()
            break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")
    elif opcao == 3:  # Excluir Produto
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            excluir.excluir_produto()
            break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    elif opcao == 4:  # Listar Estoque
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            listar.listar_produtos()
            break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    elif opcao == 5:  # Comprar Produto
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            comprar.comprar_produto()
            break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    elif opcao == 6:  # Vender Produto
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            vender.vender_produto()
            break
          elif menu == 2:
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    elif opcao == 7:  # Sair
        voltar = 0
        while voltar != 2:
          print("Deseja realmente encerrar o programa? [S/N]")
          menu = input("=> ").upper()
          if (menu == 'S'):
            print("\nSaindo...")
            exit()
          elif (menu == 'N'):
            break
          else:
            print("\033[31mOpção Inválida\33[m")

    else:
        print("\n\033[31mOpção Inválida! Tente Novamente\033[m")
