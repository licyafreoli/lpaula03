soma = 0
while True:
    try:
        numero = float(input("digite um número(negativo para sair): "))
        if numero <0:
         break
        soma += numero
    except ValueError:
       print("por favor, digite um número válido.")
print(f"a soma dos números positivos é:{soma}")