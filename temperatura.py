temperatura = int(input("Digite a temperatura atual em °C:"))

if temperatura < 18:
    print("Temperatura: Baixa")
    print("Sugestão: Considere ligar o aquecedor.")
elif temperatura > 18 and temperatura <= 25:
    print("Adequada")
    print("Sugestão: Não é necessário ajustar o controle climático.")
elif temperatura > 25:
    print("Temperatura: Alta")
    print("Sugestão: Considere ligar o ar-condicionado.")