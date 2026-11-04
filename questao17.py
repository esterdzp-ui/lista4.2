pontos = int(input("Digite os pontos do jogador:"))
nivel = 1
vida = 100

if pontos > 1000:
  nivel = 2
  vida += 100

print(f"Nível:{nivel} | Vida:{vida}")
