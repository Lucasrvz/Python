def agendar_servico(servico, preco):
    print(f"Serviço selecionado: {servico}")
    data = input(f"Digite a data para realizar o serviço de {servico}: ")
    print(f"Serviço de {servico} marcado para {data} com sucesso.")
    menu()

def listar_servicos():
    servicos = {
        "Banho": 25.00,
        "Tosa": 35.00,
        "Consulta Veterinária": 100.00,
        "Fotografia Profissional para Pets": 150.00
    }
    print("=== Listar Serviços ===")
    for servico, preco in servicos.items():
        print(f"{servico} - R${preco:.2f}")

def produtos():
    itens = {
        "Ração para cães adultos": 29.90,
        "Ração para cães filhotes": 19.90,
        "Ração para gatos adultos": 21.90,
        "Ração para gatos filhotes": 15.90
    }
    for item, preco in itens.items():
        print(f"{item} - R${preco:.2f} 1Kg")

def comprar_produto():
    carrinho = {}
    produtos = {
        "1": ("Ração para cães adultos", 29.90),
        "2": ("Ração para cães filhotes", 19.90),
        "3": ("Ração para gatos adultos", 21.90),
        "4": ("Ração para gatos filhotes", 15.90)
    }

    while True:
        print("=== Comprar Produto ===")
        for chave, (produto, preco) in produtos.items():
            print(f"{chave}. {produto} - R${preco:.2f}")
        print("0. Sair")
        
        opcao = input("Digite o número do produto que deseja comprar: ")
        
        if opcao == '0':
            break
        elif opcao in produtos:
            produto, preco = produtos[opcao]
            quantidade = int(input(f"Digite quantas unidades de {produto} deseja comprar: "))
            carrinho[produto] = carrinho.get(produto, 0) + quantidade
            print(f"{quantidade} unidades de {produto} foram adicionadas ao carrinho.")
        else:
            print("Opção inválida, por favor digite novamente.")
    
    if carrinho:
        print("\n=== Carrinho de Compras ===")
        for produto, quantidade in carrinho.items():
            print(f"{produto} x{quantidade}")
    menu()

def menu():
    while True:
        print("=== Menu do Petshop ===")
        print("1. Listar Produtos")
        print("2. Comprar Produto")
        print("3. Listar Serviços")
        print("4. Agendar Serviço")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("Listar Produtos")
            produtos()
        elif opcao == '2':
            print("Comprar Produto")
            comprar_produto()
        elif opcao == '3':
            print("Listar Serviços")
            listar_servicos()
        elif opcao == '4':
            print("Agendar Serviço")
            servicos = {
                "1": ("Banho", 25.00),
                "2": ("Tosa", 35.00),
                "3": ("Consulta Veterinária", 100.00),
                "4": ("Fotografia Profissional para Pets", 150.00)
            }
            while True:
                print("=== Agendar Serviços ===")
                for chave, (servico, preco) in servicos.items():
                    print(f"{chave}. {servico} - R${preco:.2f}")
                print("0. Sair")
                
                opcao = input("Escolha uma opção: ")
                if opcao == '0':
                    break
                elif opcao in servicos:
                    servico, preco = servicos[opcao]
                    agendar_servico(servico, preco)
                else:
                    print("Opção inválida, por favor digite novamente.")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor digite novamente.")

menu()