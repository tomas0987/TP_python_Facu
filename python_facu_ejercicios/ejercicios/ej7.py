producto=float(input('ingrese el valor del producto:'))
abono=float(input('ingrese con cuanto abona el producto:'))
if abono>producto:
    print('el cambio que le corresponde es: ', abono-producto)
elif abono<producto:
    print('el monto que falta para completar el pago es de: ', producto-abono)
else:
    print('el pago se ha realizado correctamente')
    