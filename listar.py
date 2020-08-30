import main

def exibir_produto(codigo):
    for produto in main.estoque:
        if produto[0] == codigo:
            print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')
            print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')

def listar_produtos():
    qtd_cadastrados=0
    qtd_estoque=0
    total = 0
    print("\nCÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
    print(6 * '-', '', 9 * '-', ' ', 22 * '-')
    for produto in main.estoque:
      if int(produto[2]) < 100:
        qtd_estoque+=1 
        qtd_cadastrados+=1
        print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
      else:
        print(f" {produto[0].ljust(6)}  {produto[1].ljust(20)} {produto[2]}")
        qtd_cadastrados+=1
    print(6 * '-', '', 9 * '-', ' ', 22 * '-')
    print("\nTotal de produtos cadastrados: ", qtd_cadastrados)
    print("Quantidade de itens em estoque: ", sum(main.quantidade))
    print("Produto com estoque abaixo do mínimo permitido (100 unidades): ", qtd_estoque)

