numero = input("Ingrese un número: ")
lista = list(numero)[::-1]   

resultado = ""
contador = 0

for letra in lista:
    if contador == 3:
        resultado += "."
        contador = 0
    resultado += letra
    contador += 1

resultado = resultado[::-1] 
print(resultado)
