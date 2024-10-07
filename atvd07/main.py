numero = int(input("type a number:"))

contador = 1 

while contador <=10:
    resultado = numero * contador

    if resultado % 3 == 0:
     print(f"{numero} x {contador} = {resultado}")
    contador +=1