suma=0
contador=0
num=0
while num==0:
    alumno=float(input('ingrese el numero del alumno: (ingrese 0 para salir) '))
    if alumno==0:
        print('saliendo del programa...')
        break
    elif alumno==contador:
        print('el numero del alumno ingresado ya existe, por favor ingrese un numero diferente')
        
    else:
        nota=float(input('ingrese la nota del alumno: '))
        suma=suma+nota
        contador=contador+1
print('el promedio de las notas es: ', suma/contador)
print('el total de alumnos ingresados es: ', contador)
