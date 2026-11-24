produtos = [
    ('Caneta', 2.50),
    ('Caderno', 18.90),
    ('Mochila', 45.90),
    ('Borracha', 3.00)
]

vendas = [
    ['Caderno', 10, '2026-01-15'],
    ['Caderno', 12, '2026-02-10'],
    ['Caderno', 8, '2026-03-05'],
    ['Caderno', 14, '2026-04-05'],
    ['Caderno', 16, '2026-05-01'],
    ['Caderno', 18, '2026-06-15'],
    ['Caderno', 20, '2026-07-10'],

    ['Caneta', 40, '2026-02-20'],
    ['Caneta', 30, '2026-03-10'],
    ['Caneta', 20, '2026-04-05'],
    ['Caneta', 10, '2026-05-01'],
    ['Caneta', 5, '2026-06-15'],
    ['Caneta', 15, '2026-07-10'],

    ['Mochila', 35, '2026-02-05'],
    ['Mochila', 42, '2026-03-12'],
    ['Mochila', 38, '2026-04-18'],
    ['Mochila', 45, '2026-05-20'],

    ['Borracha', 3, '2026-02-08'],
    ['Borracha', 5, '2026-03-15'],
    ['Borracha', 4, '2026-04-10'],
    ['Borracha', 6, '2026-05-14'],
]

continuar = True


def mostrar_menu(qtd_produtos):
    print('=== MENU ===')
    print(f'Produtos cadastrados: {qtd_produtos}')
    print('1 - Cadastrar produto')
    print('2 - Consultar produto')
    print('3 - Listar produtos')
    print('4 - Consultar desempenho de vendas')
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


def calcular_media_vendas(vendas, nome):
    quantidades = []

    for item in vendas:
        if item[0].lower() == nome.lower():
            quantidades.append(item[1])

    if len(quantidades) == 0:
        return None

    return sum(quantidades) / len(quantidades)


def classificar_desempenho(media):
    if media is None:
        return 'Sem histórico'
    elif media >= 30:
        return 'Alto'
    elif media >= 10:
        return 'Médio'
    else:
        return 'Baixo'


def consultar_desempenho(vendas):
    nome = input('Nome do produto: ').strip()
    media = calcular_media_vendas(vendas, nome)
    desempenho = classificar_desempenho(media)

    print('Produto:', nome)
    if media is None:
        print('Média de vendas: Sem histórico')
    else:
        print('Média de vendas:', media)
    print('Desempenho:', desempenho)

while continuar:
    mostrar_menu(len(produtos))
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_produto(produtos)
    elif opcao == '2':
        consultar_produto(produtos)
    elif opcao == '3':
            listar_produtos(produtos)
    elif opcao == '4':
        consultar_desempenho(produtos)
    elif opcao == '0':
        continuar = False
        print('Encerrando o programa...')
    else:
        print('Opção inválida...')