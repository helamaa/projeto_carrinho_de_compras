nomes = []
precos = []

print("=" * 40)
print(" Bem-vindos ao Programa de Carrinho de Compras!")
print("=" * 40)

while True:

    print("\nSelecione uma das seguintes ações:")
    print("1. Adicionar item")
    print("2. Ver carrinho")
    print("3. Remover item")
    print("4. Calcular o total")
    print("5. Sair")

    opcao = input("Por favor, insira uma ação: ")


    if opcao == "1":
        nome = input("Qual item você gostaria de adicionar? ")

        while True:
            try:
                preco = float(input(f"Qual é o preço de '{nome}'? R$ "))
                break
            except ValueError:
                print("Digite um preço válido.")

        nomes.append(nome)
        precos.append(preco)

        print(f"O item '{nome}' foi adicionado ao carrinho.")


    elif opcao == "2":

        if len(nomes) == 0:
            print("\nSeu carrinho está vazio.")
        else:
            print("\nO conteúdo do carrinho de compras é:\n")

            for i in range(len(nomes)):
                print(f"{i + 1}. {nomes[i]:20} - R$ {precos[i]:.2f}")


    elif opcao == "3":

        if len(nomes) == 0:
            print("\nO carrinho está vazio.")
        else:

            print("\nO conteúdo do carrinho de compras é:\n")

            for i in range(len(nomes)):
                print(f"{i + 1}. {nomes[i]:20} - R$ {precos[i]:.2f}")

            try:
                remover = int(input("\nQual item você gostaria de remover? "))

                indice = remover - 1

                if 0 <= indice < len(nomes):
                    nomes.pop(indice)
                    precos.pop(indice)
                    print("Item removido.")
                else:
                    print("Desculpe, esse número de item não é válido.")

            except ValueError:
                print("Digite apenas números.")


    elif opcao == "4":

        total = 0

        for preco in precos:
            total += preco

        print(f"\nO preço total dos itens no carrinho de compras é de R$ {total:.2f}")

    elif opcao == "5":
        print("\nObrigado. Até mais.")
        break 

    else:
        print("Opção inválida. Tente novamente.")