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

# TODO: exclu
# TODO: essa é uma questão de verificação do código na lista

while menu != 7:
    print("\nMenu")
    opcao = int(input("\t1 - Cadastrar Produto\n\t2 - Alterar Produto\n\t3 - Excluir Produto""\n\t4 - Listar Estoque\n\t5 - Comprar Produto""\n\t6 - Vender Produto\n\t7 - Sair\n\nDigite a opção desejada: "))
    if opcao == 1: #Cadastrar Produto
        _codigo = input("Código do produto: ")
        codigo.append(_codigo)
        if codigo in estoque:
            print("\033[31mCódigo já cadastrado\033[m")
        else:
          descricao = input("Descrição do produto: ").upper()
          quantidade = input("Quantidade de estoque: ")
          estoque.append([_codigo, descricao, quantidade])
          while int(quantidade) <= 0:
              print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
              quantidade = input("Quantidade de estoque: ")
          print(estoque)

    elif opcao == 2: #Alterar Produto
        alterar.alterar_produto()

    elif opcao == 3: #Excluir Produto
        excluir.excluir_produto()

    elif opcao == 4: #Listar Estoque
        listar.listar_produtos()

    elif opcao == 5: #Comprar Produto
        comprar.comprar_produto()

    elif opcao == 6: #Vender Produto
        vender.vender_produto()

    elif opcao == 7: #Sair
        print("\nSaindo...")
        exit()

    else:
        print("\n\033[31mOpção Inválida! Tente Novamente\033[m")