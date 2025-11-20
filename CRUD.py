def criar_despesa(lista, data, categoria, descricao, valor, forma_pagamento, pago):
    nova_despesa = {
        "id": len(lista) + 1,
        "data": data,
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor,
        "forma_pagamento": forma_pagamento,
        "pago": pago
    }
    lista.append(nova_despesa)
    return nova_despesa


def listar_despesas(lista):
    return lista


def atualizar_despesa(lista, id_alvo, novos_dados):
    for despesa in lista:
        if despesa["id"] == id_alvo:
            despesa.update(novos_dados)
            return True
    return False


def excluir_despesa(lista, id_alvo):
    for despesa in lista:
        if despesa["id"] == id_alvo:
            lista.remove(despesa)
            return True
    return False


# extra

def total_por_categoria(lista):
    resultado = {}
    for d in lista:
        cat = d["categoria"]
        resultado[cat] = resultado.get(cat, 0) + d["valor"]
    return resultado


def resumo_mensal(lista, mes):
    total = 0
    qtd = 0

    for d in lista:
        if d["data"].startswith(mes): 
            total += d["valor"]
            qtd += 1

    media = total / qtd if qtd > 0 else 0
    return total, qtd, media
