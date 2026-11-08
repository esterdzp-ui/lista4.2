
# EXERCÍCIO 20: Desafio de Coordenadas
# Enunciado: No Godot, queremos evitar que o personagem saia da tela.
# Se a posicao_x for menor que 0 ou maior que 1024, imprima "Atenção: Saindo da tela!".

# ENTRADA
posicao_x = int(input("Digite a posição X do personagem: "))

# PROCESSAMENTO + SAÍDA
if posicao_x < 0 or posicao_x > 1024:
    print("Atenção: Saindo da tela!")
else:
    print("Dentro da tela")
