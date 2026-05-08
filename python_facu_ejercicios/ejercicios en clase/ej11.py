import math
numa=0
while numa==0:
    print('1. calcular seno')
    print('2. calcular coseno')
    print('3. calcular tangente')
    print('4. para salir')
    num=int(input('ingrese el numero de la operacion que desea realizar: '))
    if num==1:
        angulo=float(input('ingrese el angulo en grados: '))
        angulo_rad=math.radians(angulo)
        resultado=math.sin(angulo_rad)
        print('el seno del angulo es: ', resultado)
    elif num==2:
        angulo=float(input('ingrese el angulo en grados: '))
        angulo_rad=math.radians(angulo)
        resultado=math.cos(angulo_rad)
        print('el coseno del angulo es: ', resultado)
    elif num==3:
        angulo=float(input('ingrese el angulo en grados: '))
        angulo_rad=math.radians(angulo)
        resultado=math.tan(angulo_rad)
        print('la tangente del angulo es: ', resultado)
    elif num==4:
        numa=1
    else:
        print('opcion invalida')

