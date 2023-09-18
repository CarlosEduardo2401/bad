# Solicita as dimensões do aposento ao usuário
largura_aposento = float(input("Digite a largura do aposento em metros: "))
comprimento_aposento = float(input("Digite o comprimento do aposento em metros: "))

# Altura do pé-direito do aposento
altura_pe_direito = 2.80  # metros

# Área das paredes a serem pintadas (desconsiderando a porta)
area_paredes = 2 * (largura_aposento + comprimento_aposento) * altura_pe_direito

# Dimensões da porta
largura_porta = 0.80  # metros
altura_porta = 2.10  # metros

# Área da porta
area_porta = largura_porta * altura_porta


area_paredes -= area_porta


quantidade_tinta_por_lata = float(input("Digite a quantidade de tinta por lata em litros: "))


litros_tinta_necessarios = area_paredes / 3


quantidade_latas_tinta = litros_tinta_necessarios / quantidade_tinta_por_lata


import math
quantidade_latas_tinta = math.ceil(quantidade_latas_tinta)
print(f"Quantidade de latas de tinta necessárias: {quantidade_latas_tinta}")
