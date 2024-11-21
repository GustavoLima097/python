while True:
    # Solicita um número ao usuário
    numero = int(input("Digite um número (ou um número negativo para encerrar): "))
    
    # Encerra o programa se o número for negativo
    if numero < 0:
        print("Programa encerrado.")
        break
    
    # Pula a verificação se o número for menor que 2
    if numero < 2:
        print(f"{numero} não é primo.")
        continue
    
    # Verifica se o número é primo
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break
    else:
        print(f"{numero} é primo.")
