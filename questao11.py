# EXERCÍCIO 11: Sistema de Notas
# Enunciado: Crie um programa que receba a nota de um aluno:
# ● Se for 7 ou mais: "Aprovado".
# ● Se for entre 5 e 6.9: "Recuperação".
# ● Se for menor que 5: "Reprovado".

# ENTRADA
nota = float(input("Digite a nota do aluno: "))

# PROCESSAMENTO + SAÍDA
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
