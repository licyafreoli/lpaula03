somas = 0
contador = 0

while True:
    nota = float(input("Digite a nota do aluno (-1 para sair): "))
    
    if nota == -1:
        break
    
    if 0 <= nota <= 10:
        somas += nota
        contador += 1
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

if contador > 0:
    media = somas / contador
    print(f"A média das notas inseridas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
