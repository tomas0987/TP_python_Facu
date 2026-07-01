lista=[]
valor=0
while valor==0:
    numero=int(input("ingrese un numero: "))
    if numero== -1:
        valor=1
    else:
        lista.append(numero)
print("el mayor es: ", max(lista))
print("el menor es:",min(lista))

    