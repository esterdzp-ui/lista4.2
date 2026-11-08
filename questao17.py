
# EXERCÍCIO 17: Evolução de Nível
# Enunciado: Se os pontos do jogador forem maiores que 1000, mude a variável nível para 2 e dê um bônus de 100 de vida.

# ENTRADA
pontos = 1100
nivel = 1
vida = 100

# PROCESSAMENTO
if pontos > 1000:
    nivel = 2
    vida = vida + 100

# SAÍDA
print(f"Nível: {nivel} | Vida: {vida}")
