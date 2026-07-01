limite=float(input('ingrese el limite actual de su tarjeta:'))
tipo=int(input('ingrse el tipo de su tarjeta: (1,2,3,4)'))
if tipo==1:
    limite=limite*1.25
    print('el nuevo limite de su tarjeta es: ', limite)
elif tipo==2:
    limite=limite*1.35
    print('el nuevo limite de su tarjeta es: ', limite)
elif tipo==3:
    limite=limite*1.40
    print('el nuevo limite de su tarjeta es: ', limite)
elif tipo==4:
    limite=limite*1.50
    print('el nuevo limite de su tarjeta es: ', limite)
else:
    print('el tipo de tarjeta ingresada no es valida')
    