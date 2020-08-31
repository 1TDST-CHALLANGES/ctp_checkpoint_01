import variavel

menu = 0

while menu != 7:
    print("\nMenu")
    opcao = int(input(
        "\t1 - Cadastrar Produto\n\t2 - Alterar Produto\n\t3 - Excluir Produto""\n\t4 - Listar Estoque\n\t5 - Comprar "
        "Produto""\n\t6 - Vender Produto\n\t7 - Sair\n\nDigite a opção desejada: "))
    if opcao == 1:  # Cadastrar Produto
        voltar = 0
        while voltar != 2:
          print("1 - Continuar    2 - Voltar")
          menu = int(input("=>"))
          if menu == 1:
            variavel.cadastrar()
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
            variavel.alterar()
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
            variavel.excluir()
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
            variavel.listar_produtos()
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
            variavel.comprar()
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
            variavel.vender()
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
