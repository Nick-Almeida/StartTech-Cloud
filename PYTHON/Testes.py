# # Exercício 1

# nota1 = float(input("Digite sua primeira nota:\n"))
# nota2 = float(input("Digite sua segunda nota:\n"))
# nota3 = float(input("Digite sua terceira nota:\n"))
# nota4 = float(input("Digite sua quarta nota:\n"))
# media = (nota1 + nota2 + nota3 + nota4) / 4
    
# print("A média das suas notas notas é:", media)

# # ----------------------------------------------------------------

# # Exercício 2

# centimetros = float(input("Digite a medida em centímetros:\n"))
# metros = centimetros / 100
# print("A medida em metros é:", metros)

# # ----------------------------------------------------------------

# # Exercício 3

# valor_hora = float(input("Digite o valor da hora trabalhada:\n"))
# horas = int(input("Digite o número de horas trabalhadas:\n"))
# salario = horas * valor_hora
# print("O salário a receber no fim do mês é:", salario)

# ----------------------------------------------------------------

# Exercício 4

# celsius = float(input("Digite a temperatura em graus Celsius:\n"))
# fahrenheit = (celsius * 9/5) + 32
# print(f"A temperatura de {celsius}ºC em graus Fahrenheit é: {fahrenheit}ºF")

# ----------------------------------------------------------------

# Exercício 5

# usuario = "Admin"
# senha = "123456"

# usuario_input = input("Digite o nome de usuário:\n")
# senha_input = input("Digite a senha:\n")
# mensagem = (usuario_input == usuario and senha_input == senha) and "Acesso permitido!" or "Acesso negado!"

# print(mensagem)

# ----------------------------------------------------------------

valor_total = float(input("Digite o valor total da compra:\n"))
cupom = input("Digite o código do cupom de desconto (ou deixe em branco se não houver):\n")

if valor_total > 100 or cupom == "DESC10":
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"Desconto aplicado: R${desconto:.2f}. Valor final da compra: R${valor_final:.2f}.")
else:
    print(f"Valor final da compra: R${valor_total:.2f}. Nenhum desconto aplicado.")