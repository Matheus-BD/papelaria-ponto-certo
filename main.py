def mostrar_menu(qtd_produtos):
    print("\n--- Menu ---")
    print(f"Produtos cadastrados: {qtd_produtos}")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos")
    print("0 - Sair")

def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco_valido = False
    while not preco_valido:
        preco = float(input("Preço do produto (maior que zero): "))
        if preco > 0:
            preco_valido = True
        else:
            print("Preço inválido. Digite um valor maior que zero.")
    produtos.insert(0, [nome, preco])
    print("Produto cadastrado com sucesso!")
    print(f"Total de produtos: {len(produtos)}")

def consultar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    encontrado = False
    i = 0
    while i < len(produtos):
        if produtos[i][0].lower() == nome_busca.lower():
            print(
                f"Produto encontrado: "
                f"{produtos[i][0]} - R$ {produtos[i][1]:.2f}"
            )
            encontrado = True
        i += 1
    if not encontrado:
        print("Produto não encontrado.")

def listar_produtos(produtos):
    print("=== Produtos cadastrados ===\n")
    for i in range(len(produtos)):
        caractres = len(produtos[i][0])
        numero_de_pontos = 15
        quantida_de_pontos = "." *(numero_de_pontos - caractres)
        print(f"{i}. {produtos[i][0]} {quantida_de_pontos} R${produtos[i][1]:.2f}")
produtos = []
continuar = True

print(f"´" * 15)

while continuar:
    mostrar_menu(len(produtos))
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_produto(produtos)
    elif opcao == "2":
        consultar_produto(produtos)
    elif opcao == "3":
        listar_produtos(produtos)
    elif opcao == "0":
        continuar = False
    else:
        print("Opção inválida.")