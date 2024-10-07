while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    
    if 1 <= numero <= 10:
        print(f"Número {numero} é válido!")
        break 
    else:
        print("Número inválido! Tente novamente.")
