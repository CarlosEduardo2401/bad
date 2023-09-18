

pontos_necessarios = int(input("Digite a quantidade de pontos necessários (em mil unidades): "))


cotacao_dolar = float(input("Digite a cotação do dólar atual: "))

gastos_em_dolares = pontos_necessarios / 1.5
gastos_em_reais = gastos_em_dolares * cotacao_dolar

# Exibe o valor em reais que o usuário terá que gastar
print(f"Para obter {pontos_necessarios} pontos, o usuário terá que gastar R$ {gastos_em_reais:.2f}.")

