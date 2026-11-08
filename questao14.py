# EXERCÍCIO 14: Verificador de Número Positivo
# Enunciado: Escreva um código que diga se um número digitado é positivo, negativo ou zero.

# ENTRADA
valor = float(input("Digite um número: "))

# PROCESSAMENTO + SAÍDA
if valor > 0:
    print("Número positivo")
elif valor < 0:
    print("Número negativo")
else:
    print("É zero")
