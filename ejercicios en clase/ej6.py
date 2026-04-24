cantboleto=float(input('ingrese la cantidad de boletos que desea comprar:'))
cantidad=5
valor=100
if cantboleto>cantidad:
    print('la cantidad de boletos disponibles es menor')
else:
    total=cantboleto*valor
    print('el valor total de su compra es: ', total)
    cantidad= cantidad-cantboleto
    print('la cantidad de boletos disponibles es: ', cantidad)