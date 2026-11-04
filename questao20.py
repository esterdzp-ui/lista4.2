# Entrada
posicao_x = int(input("Digite a posição X: "))

# Processamento e Saída
if posicao_x < 0 or posicao_x > 1024:
    print("Atenção: Saindo da tela!")
else:
    print("Dentro da tela.")
