from CRUD import (
    criar_despesa,
    listar_despesas,
    atualizar_despesa,
    excluir_despesa,
    total_por_categoria,
    resumo_mensal
)

# Aqui ficam as despesas na memória
despesas = []

def menu():
    print("\n========================")
    print("   CONTROLE DE DESPESAS")
    print("========================")
    print("1 - Cadastrar despesa")
    print("2 - Listar despesas")
    print("3 - Atualizar despesa")
    print("4 - Excluir despesa")
    print("5 - Total por categoria (extra)")
    print("6 - Resumo mensal (extra)")
    print("7 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR DESPESA ---")
        data = input("Data (YYYY-MM-DD): ")
        categoria = input("Categoria: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        forma_pagamento = input("Forma de pagamento: ")
        pago = input("Pago? (s/n): ").lower() == "s"

        criar_despesa(despesas, data, categoria, descricao, valor, forma_pagamento, pago)
        print("Despesa cadastrada com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE DESPESAS ---")
        for d in listar_despesas(despesas):
            print(d)

    elif opcao == "3":
        print("\n--- ATUALIZAR DESPESA ---")
        id_despesa = int(input("ID da despesa: "))
        print("Deixe vazio para não alterar o campo.")
        
        nova_data = input("Nova data: ")
        nova_categoria = input("Nova categoria: ")
        nova_desc = input("Nova descrição: ")
        novo_valor = input("Novo valor: ")
        nova_forma = input("Nova forma de pagamento: ")
        pago_raw = input("Pago? (s/n): ")

        novos_dados = {}

        if nova_data: novos_dados["data"] = nova_data
        if nova_categoria: novos_dados["categoria"] = nova_categoria
        if nova_desc: novos_dados["descricao"] = nova_desc
        if novo_valor: novos_dados["valor"] = float(novo_valor)
        if nova_forma: novos_dados["forma_pagamento"] = nova_forma
        if pago_raw: novos_dados["pago"] = pago_raw.lower() == "s"

        if atualizar_despesa(despesas, id_despesa, novos_dados):
            print("Despesa atualizada!")
        else:
            print("ID não encontrado.")

    elif opcao == "4":
        print("\n--- EXCLUIR DESPESA ---")
        id_despesa = int(input("ID da despesa: "))
        if excluir_despesa(despesas, id_despesa):
            print("Despesa excluída!")
        else:
            print("ID não encontrado.")

    elif opcao == "5":
        print("\n--- TOTAL POR CATEGORIA ---")
        totals = total_por_categoria(despesas)
        for cat, valor in totals.items():
            print(f"{cat}: R$ {valor:.2f}")

    elif opcao == "6":
        print("\n--- RESUMO MENSAL ---")
        mes = input("Informe o mês (YYYY-MM): ")
        total, qtd, media = resumo_mensal(despesas, mes)
        print(f"Total gasto: R$ {total:.2f}")
        print(f"Quantidade de despesas: {qtd}")
        print(f"Média por despesa: R$ {media:.2f}")

    elif opcao == "7":
        print("Encerrando...")
        break

    else:
        print("Opção inválida. Tente novamente.")
