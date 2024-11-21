# Inicializa variáveis
soma = 0
contagem = 0

# Loop para solicitar números até que o usuário digite 0
while True:
    numero = float(input("Digite um número (ou 0 para encerrar): "))
    
    # Encerra o loop se o número for 0
    if numero == 0:
        break
    
    # Adiciona o número à soma e incrementa a contagem
    soma += numero
    contagem += 1

# Calcula a média, se houver pelo menos um número inserido
if contagem > 0:
    media = soma / contagem
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número válido foi digitado.")
