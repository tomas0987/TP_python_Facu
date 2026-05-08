n = int(input("ingrese un numero: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("el factorial de ", n, "es: ", factorial(n))