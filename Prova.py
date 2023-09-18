
pontuacao = int(input("Digite a pontuação do aluno (0 a 100): "))


if 0 <= pontuacao <= 49:
    conceito = "D"
elif 50 <= pontuacao <= 69:
    conceito = "C"
elif 70 <= pontuacao <= 80:
    conceito = "B"
elif 90 <= pontuacao <= 100:
    conceito = "A"
else:
    conceito = "Pontuação inválida"


print(f"Conceito: {conceito}")

