# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Solicita um número e um texto ao usuário
numero = int(input("Digite um número: "))
texto = input("Digite um texto: ")

# Repete o texto 'numero' vezes, separando por espaço
for i in range(numero):
    if i == numero - 1:
        print(texto)
    else:
        print(texto, end=" ")
