# EXERCÍCIO 13: Validação de Login
# Enunciado: Crie uma variável senha_mestra = "python123". Peça ao usuário para digitar uma senha e use um if para verificar se ele acertou.

# ENTRADA
senha_mestra = "python123"
senha_digitada = input("Digite a senha: ")

# PROCESSAMENTO + SAÍDA
if senha_digitada == senha_mestra:
    print("Senha correta! Login liberado")
else:
    print("Senha errada! Acesso negado")
