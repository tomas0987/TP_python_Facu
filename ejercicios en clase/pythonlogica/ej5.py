def potencia(a,b):
    if b ==0:
        return 1
    else:
        return a* potencia(a,b-1)
a= int(input("ingrese la base: "))
b= int(input("ingrese el exponente: "))
print("el resultado de ", a, "elevado a ", b, "es: ", potencia(a,b))
