n=int(input("ingrese un numero para calcular el factorial"))
def factorial(n):
    if n==0:
        return 1
    
    else:
        return n*factorial(n-1)
print(f"el factorial de {n} es {factorial(n)}")