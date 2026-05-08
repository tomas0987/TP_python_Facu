def contador(n):
    if n == 0:
        return
    else:
        contador(n - 1)   # Llamada recursiva primero
        print(n)          # Se imprime al "volver" de la recursión

n = int(input("Ingrese un número: "))
print("Los números desde 1 hasta", n, "son:")
contador(n)
