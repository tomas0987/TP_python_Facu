cantempleados=0
cantempleadoscobranmas200000=0
cantiemplecobranmasde50000yson3cat=0
sueldoTotal=0
sueldos=[]
bucle=True
cat1=0
cat2=0
cat3=0
promedio=0

mayorsueldo=0
empleado_mayor=""
minorsueldo=999999

while bucle==True:
    
    empleado=str(input("ingrese el nombre del empleado: "))
    cantempleados=cantempleados+1

    sueldo=float(input("ingrese el sueldo del empleado: "))
    sueldoTotal=sueldoTotal+sueldo
    sueldos.append(sueldo)

    categoria=int(input("ingrese la categoria del empleado (1, 2 o 3): "))

    # Sueldos por categoría
    if categoria==1: 
        cat1=cat1+sueldo
    elif categoria==2:
        cat2=cat2+sueldo
    else:
        cat3=cat3+sueldo

    # Contadores correctos (afuera del else)
    if sueldo>200000:
        cantempleadoscobranmas200000+=1
    if sueldo>50000 and categoria==3:
        cantiemplecobranmasde50000yson3cat+=1

    # Mayor sueldo
    if sueldo > mayorsueldo:
        mayorsueldo = sueldo
        empleado_mayor = empleado

    # Menor sueldo
    if sueldo < minorsueldo:
        minorsueldo = sueldo

    sigue=str(input("desea ingresar otro empleado? (si/no): "))
    if sigue=="no":
         bucle=False

promedio= sueldoTotal/cantempleados
        
print("el sueldo total de la empresa es: ", sueldoTotal)
print("el sueldo promedio de la empresa es: ", promedio)
print("el mayor sueldo de la empresa es: ", mayorsueldo, "y lo cobra: ", empleado_mayor)
print("el menor sueldo de la empresa es: ", minorsueldo)
print("la cantidad de empleados que cobran mas de 200000 es: ", cantempleadoscobranmas200000)
print("la cantidad de empleados que cobran mas de 50000 y son de categoria 3 es: ", cantiemplecobranmasde50000yson3cat)
print("el total de sueldos de la categoria 1 es: ", cat1)
print("el total de sueldos de la categoria 2 es: ", cat2)
print("el total de sueldos de la categoria 3 es: ", cat3)
