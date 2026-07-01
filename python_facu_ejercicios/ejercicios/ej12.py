valorMensual=float(input("ingrese el valor mensual del alquiler:"))
meses=int(input("ingrese la cantidad de meses a alquilar:"))
incremento=float(input("ingrese el porcentaje de incremento mensual:"))
i=meses

for i in range(meses):
    valorMensual=valorMensual+(valorMensual*(incremento/100))
    print("el valor mensual del alquiler para el mes", i+1, "es:", valorMensual)
    