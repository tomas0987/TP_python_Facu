numa=0
while numa==0:
    valor=float(input('ingrese el valor del producto: '))
    if valor==0:
        print('saliendo del programa...')
        break
    elif valor != 0:
        print('el valor del producto es: ', valor)
        abono=float(input('ingrese el valor del abono: '))
        if abono==valor:
            print('el producto ha sido pagado en su totalidad')
        elif abono<valor:
            print('el producto no ha sido pagado en su totalidad, el valor restante es: ', valor-abono)
        elif abono>valor:
            print('el abono ingresado es mayor al valor del producto, el cambio a devolver es: ', abono-valor)
        
            