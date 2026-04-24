n= int (input("ingrese un numero: "))

def contador(n):
    if n == 0 :
        return 0
    else:
        print(n)
        return contador(n-1)
print("los numeros hasta ", n, "son: ")
contador(n)