suma=0
valor=0
contador=0
while valor==0:
    costo=float(input('ingrese el costo del producto: '))
    if costo==0:
        print('saliendo del programa...')
        break
    else:
        suma=suma+costo
        contador=contador+1
print('el costo total de los productos es: ', suma)
print("el total de productos ingresados es: ", contador)
