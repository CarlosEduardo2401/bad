# Solicita dois números inteiros ao usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Calcula a soma dos números
soma = numero1 + numero2

# Verifica se a soma é maior ou menor que 1000
if soma > 1000:
    print(f"A soma dos números {numero1} e {numero2} é {soma}, que é maior do que 1000.")
elif soma < 1000:
    print(f"A soma dos números {numero1} e {numero2} é {soma}, que é menor do que 1000.")
else:
    print(f"A soma dos números {numero1} e {numero2} é igual a 1000.")
