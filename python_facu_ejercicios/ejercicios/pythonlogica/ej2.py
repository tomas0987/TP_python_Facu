
n= int(input("ingrese un numero: "))

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
print("la suma de los numeros hasta ", n, "es: ", suma(n))
