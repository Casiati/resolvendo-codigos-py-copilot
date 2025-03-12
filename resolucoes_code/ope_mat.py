# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário qual operação deseja realizar
print("Escolha a operação:")
print("1. Soma")
print("2. Subtração (com valores absolutos)")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite o número da operação (1/2/3/4): ")

# Realiza a operação com base na escolha do usuário
if operacao == '1':
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
elif operacao == '2':
    resultado = abs(num1 - num2)
    print(f"A subtração de {num1} e {num2} com valor absoluto é: {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é: {resultado}")
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é: {resultado}")
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida! Escolha uma operação válida (1/2/3/4).")

