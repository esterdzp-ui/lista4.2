# EXERCÍCIO 16: Cálculo de Dano com Escudo
# Enunciado: Se o jogador tem um escudo_ativo = True, ele recebe apenas 50% do dano.
# Se for False, recebe 100%. Escreva a lógica que calcula o dano_final baseado em um dano_base = 20.
# ENTRADA
escudo_ativo = True
dano_base = 20
# PROCESSAMENTO
if escudo_ativo:
     dano_final = dano_base * 0.5
else:
     dano_final = dano_base
# SAÍDA
print(f"Dano recebido: {dano_final}")
