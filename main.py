produtos = []
continuar = True

def mostrar_menu():
    print('===MENU===')
    print('1 - Cadastrar produto')
    print('2 - Consultar produto')
    print('0 - Sair')

def cadastrar_produto(produtos):
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    produtos.append((nome, preco))
    print('Produto cadastrado com sucesso!')

while continuar:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_produto(produtos)
    elif opcao == "2":
        print("Função de consulta ainda será implementada.")
    elif opcao == "0":
        continuar = False
    else:
        print("Opção inválida...")