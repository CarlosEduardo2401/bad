
preco_alcool = 1.7997  # Preço do álcool por litro
preco_diesel = 0.9798  # Preço do diesel por litro
preco_gasolina = 2.1009  # Preço da gasolina por litro

# Solicita o tipo de combustível ao usuário
tipo_combustivel = input("Digite o tipo de combustível (a para Álcool, d para Diesel, g para Gasolina): ").lower()

# Verifica o tipo de combustível e solicita a quantidade em litros
if tipo_combustivel == 'a':
    litros = float(input("Digite a quantidade em litros: "))
    valor_a_pagar = litros * preco_alcool
elif tipo_combustivel == 'd':
    litros = float(input("Digite a quantidade em litros: "))
    valor_a_pagar = litros * preco_diesel
elif tipo_combustivel == 'g':
    litros = float(input("Digite a quantidade em litros: "))
    valor_a_pagar = litros * preco_gasolina
else:
    print("Tipo de combustível inválido.")
    exit()

# Exibe o valor a ser pago pelo combustível
print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")
