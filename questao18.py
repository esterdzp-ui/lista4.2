# EXERCÍCIO 18: Diálogo de RPG
# Enunciado: Crie um menu onde o jogador escolhe entre 1 (Falar), 2 (Atacar) ou 3 (Fugir).
# Use if/elif/else para exibir uma resposta diferente para cada escolha.
# ENTRADA
escolha = int(input("Escolha: 1‑Falar | 2‑Atacar | 3‑Fugir: "))
# PROCESSAMENTO + SAÍDA
if escolha == 1:
     print("Você conversa com o NPC")
elif escolha == 2:
     print("Você parte para o ataque!")
elif escolha == 3:
     print("Você foge da batalha!")
else:
     print("Opção inválida")
