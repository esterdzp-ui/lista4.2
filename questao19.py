# Entrada
peso_atual = int(input("Digite o peso atual: "))
limite_maximo = 50
peso_item = 5

# Processamento
if peso_atual + peso_item > limite_maximo:
    print("Inventário Cheio!")
else:
    print("Conseguiu pegar o item!")
