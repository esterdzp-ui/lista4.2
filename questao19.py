# EXERCÍCIO 19: Limite de Inventário
# Enunciado: O jogador quer pegar um item de peso 5. Verifique se o peso_atual + 5 ultrapassa o limite_máximo de 50.
# Se ultrapassar, imprima "Inventário Cheio!".

# ENTRADA
peso_atual = 47
peso_item = 5
limite_maximo = 50

# PROCESSAMENTO + SAÍDA
if peso_atual + peso_item > limite_maximo:
    print("Inventário Cheio!")
else:
    peso_atual = peso_atual + peso_item
    print(f"Item coletado! Peso atual: {peso_atual}")
