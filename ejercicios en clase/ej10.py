valor = 0
while valor >= 0:
    valor =float(input('ingrese el valor del producto: '))
    if valor == 0:
        print('saliendo del programa...')
        break
    print('ingrese la forma de pago: ')
    print('1. efectivo: %10 de descuento')
    print('2. en un pago')
    print('3. en 3 pagos:  %5 de recargo')
    print('4. en 6 pagos: %10 de recargo')
    print('5. en 12 pagos: %15 de recargo') 
    num=int(input('ingrese el numero de la forma de pago: '))
    if num==1:
        valor=valor*0.90
        print('el valor a pagar es: ', valor)
    elif num==2:
        print('el valor a pagar es: ', valor)
    elif num==3:
        valor=valor*1.05
        print('el valor a pagar es: ', valor)
    elif num==4:
        valor=valor*1.10
        print('el valor a pagar es: ', valor)
    elif num==5:
        valor=valor*1.15
        print('el valor a pagar es: ', valor)
    else:
        print('la forma de pago ingresada no es valida')    
        