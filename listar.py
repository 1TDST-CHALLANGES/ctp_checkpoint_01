import main

def exibir_produto(codigo):
    for produto in main.estoque:
        if produto[0] == codigo:
            print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')
            print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
            print(6 * '-', '', 9 * '-', ' ', 22 * '-')

def listar_produtos():
    for produto in main.estoque:
        print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
        print(6 * '-', '', 9 * '-', ' ', 22 * '-')
        print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
        print(6 * '-', '', 9 * '-', ' ', 22 * '-')