# Checkpoint 1 - 30/08

## Projeto no browser clique no botão: [![Run on Repl.it](https://repl.it/badge/github/1TDST-CHALLANGES/ctp_checkpoint_01)](https://repl.it/github/1TDST-CHALLANGES/ctp_checkpoint_01)

## Crie um programa em Python que faça o controle de produtos da empresa XPTO.

- [x] (0.5 ponto) Exibir o seguinte menu:


      Menu:
        1 - Cadastrar produto
        2 - Alterar produto
        3 - Excluir produto
        4 - Listar estoque de peças
        5 - Comprar produto
        6 - Vender produto
        7 - Sair
      


- [x] (1.0 ponto) Caso o usuário escolha a opção 1, o programa deve solicitar o código do produto, descrição do produto e quantidade do produto em estoque. Verificar se o código já existe no cadastro, pois não pode ter código duplicado. Depois retorna para o Menu.

- [x] (1.0 ponto) Caso o usuário escolha a opção 2, o programa deve solicitar a senha de acesso para alteração. Senha de acesso: yN1825*a

Se o usuário digitar a senha correta, solicitar então o código do produto que será alterado. Se ocódigo existir, mostrar a descrição e a quantidade em estoque cadastrados. O usuário pode alterar apenas a descrição e a quantidade em estoque. Se o código não existir, mostrar a seguinte mensagem na tela: “PRODUTO NÃO CADASTRADO.” Depois retorna para o Menu. Se o usuário digitar a senha incorreta, a mensagem de alerta ao usuário deve ser: “SENHA INCORRETA”. Depois retorna para o Menu.

IMPORTANTE: SE O USUÁRIO DIGITAR 3 VEZES A SENHA INCORRETA O PROGRAMA DEVE SER FINALIZADO APÓS MOSTRAR MENSAGEM: "SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR"

- [x] (1.0 ponto) Caso o usuário escolha a opção 3, o programa deve solicitar a senha de acesso para alteração. Senha de acesso: yN1825*a

Se o usuário digitar a senha correta, solicitar então o código do produto que será alterado. Se o código existir, mostrar a descrição, a quantidade em estoque e a mensagem: "DESEJA EXCLUIR O PRODUTO?" Se sim, excluir e mostrar na tela: "PRODUTO EXCLUIDO COMSUCESSO". Se não, apenas mostrar na tela. “PRODUTO NÃO EXCLUÍDO”. Se o código não existir, mostrar a seguinte mensagem: “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu. Se o usuário digitar a senha incorreta, a mensagem de alerta ao usuário deve ser: “SENHA INCORRETA”. Depois retorna para o Menu.

IMPORTANTE: SE O USUÁRIO DIGITAR 3 VEZES A SENHA INCORRETA O PROGRAMA DEVE SER FINALIZADO APÓS EMITIR MENSAGEM: "SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR"

- [x] (1.0 ponto) Caso o usuário escolha a opção 4, o programa deve mostrar na tela todos os produtos cadastrados e no final totalizar da seguinte maneira :

      *Ordem crescente de código do produto:

      MODELO DE RELATÓRIO:
      CÓDIGO DESCRIÇÃO QUANTIDADE EM ESTOQUE:
      ————— ————————————— ———————————————-
      1001 PASTA ESCOLAR TIPO 2 102
      1002 PASTA ESCOLAR TIPO 1 97
      1003 CANETA AZUL 152

      Total de produtos cadastrados: 3
      Quantidade de itens em estoque: 351
      Produtos com estoque abaixo do mínimo permitido (100 unidades): 1

- [x] (1.0 ponto) Caso o usuário escolha a opção 5, o programa deve solicitar o código do produto. Se o código existir no cadastro, mostrar na tela a descrição e a quantidade atual em estoque. Solicitar a quantidade de produtos que deseja comprar. A quantidade digitada pelo usuário deve somar com o estoque atual do produto em questão. Se o código não existir, mostrar a seguinte mensagem: “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu.

- [x] (1.0 ponto) Caso o usuário escolha a opção 6, o programa deve solicitar código do produto. Se o código existir no cadastro, mostrar na tela a descrição e a quantidade atual em estoque. Solicitar a quantidade de produtos que deseja vender. A quantidade digitada pelo usuário deve subtrair com o estoque atual do produto em questão.

Importante: A quantidade em estoque não pode ficar negativa. Caso o usuário digite uma quantidade maior do que a que tem em estoque não permitir a venda. Se o código não existir, mostrar a seguinte mensagem: “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu.

- [x] (0.5 ponto) Caso o usuário escolha a opção 7, o programa deve ser finalizado.
   
      ——————————————————————————————————————————————————————————————————————————————————————————————————————————————

- [x] (2.0 pontos) REGRAS:
a) Obrigatório o uso de laço de repetição
b) Obrigatório criar pelo menos 2 (duas) funções e fica a critério do aluno: com ou sem parâmetro e com ou sem return.
c) Obrigatório usar lista e tupla.

- [x] (1.0 ponto) Considerações:
a) Não há limite para cadastro de produtos
b) Se o usuário entrar com a senha correta (ao acessar a opção alterar ou excluir produto), não deve ser solicitada mais até o usuário sair do programa. O limite de tentativas para acesso, em caso de senha incorreta, é 3 tentativas.
c) Não permitir quantidade de produto menor ou igual a 0 (zero) nas opções 1, 2, 5 e 6.
d) O programa somente pode ser finalizado se o usuário escolher a opção 7 ou se digitar 3 vezes a senha de acesso a opção 2 e 3 incorretamente.
