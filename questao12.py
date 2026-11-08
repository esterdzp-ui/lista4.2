# EXERCÍCIO 12: Comparando Dois Números
# Enunciado: Peça ao usuário dois números (n1 e n2). O programa deve dizer qual deles é o maior ou se são iguais.

# ENTRADA
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO + SAÍDA
if n1 > n2:
    print(f"O maior número é {n1}")
elif n2 > n1:
    print(f"O maior número é {n2}")
else:
    print("Os dois números são iguais")
