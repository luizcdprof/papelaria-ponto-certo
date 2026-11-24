produtos = [
    ('Caneta', 2.50),
    ('Caderno', 18.90),
    ('Borracha', 3.00)
]
continuar = True

def mostrar_menu(qtd_produtos):
    print('=== MENU ===')
    print(f'Produtos cadastrados: {qtd_produtos}')
    print('1 - Cadastrar produto')
    print('2 - Consultar produto')
    print('3 - Listar produtos')
    print('0 - Sair')

def cadastrar_produto(produtos):
    nome = input('Nome do produto: ')
    preco_valido = False
    while not preco_valido:
        preco = float(input('Preço do produto (maior que zero): '))
        if preco > 0:
            preco_valido = True
        else:
            print('Preço inválido. Digite um valor maior que zero.')
    produtos.insert(0, (nome, preco))
    print('Produto cadastrado com sucesso!')
    print(f'Total de produtos: {len(produtos)}')

def consultar_produto(produtos):
    nome_busca = input('Digite o nome do produto: ')
    encontrado = False
    i = 0
    while i < len(produtos) and not encontrado:
        if produtos[i][0].lower() == nome_busca.lower():
            print(
                f'Produto encontrado: '
                f'{produtos[i][0]} - R$ {produtos[i][1]:.2f}'
            )
            encontrado = True
        i += 1
    if not encontrado:
        print('Produto não encontrado.')

def listar_produtos(produtos):
    if len(produtos) == 0:
        print('Nenhum produto cadastrado.')
        return

    print('\n=== Produtos cadastrados ===')

    for i, produto in enumerate(produtos, start=1):
        print(f'{i}. {produto[0]} - R$ {produto[1]:.2f}')

    print(f'\nTotal de produtos: {len(produtos)}')
    print(f'Total de produtos: {len(produtos)}')

while continuar:
    mostrar_menu(len(produtos))
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_produto(produtos)
    elif opcao == '2':
        consultar_produto(produtos)
    elif opcao == '3':
        listar_produtos(produtos)
    elif opcao == '0':
        continuar = False
    else:
        print('Opção inválida...')