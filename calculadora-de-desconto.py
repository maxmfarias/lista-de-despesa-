valorCompra = float(input("Digite o valor total da compra: R$"))



if valorCompra > 200.00:
    desconto = valorCompra * 0.10
    valorFinal = valorCompra - desconto
    print(f"Valor original: R$ {valorCompra:.2f}")
    print(f"Desconto aplicado: {desconto:.2f}")
    print(f"Valor final: {valorFinal:.2f}")
else:
    print(f"Valor original: R$ {valorCompra:.2f}")
    print("Nenhum desconto aplicado")





