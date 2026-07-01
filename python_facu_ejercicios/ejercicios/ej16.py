contador=0
salida=0
while salida==0:
    nombre=str(input("Ingrese un nombre: "))
    if nombre=="fin":
        salida=1
    else:
        print("Bienvenido ", nombre)
        contador+=1
print("La cantidad de nombres ingresados es: ", contador)