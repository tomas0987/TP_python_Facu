meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
num_mes=int(input("ingrese un numero de mes: "))
if num_mes>0 and num_mes<13:
    print("el mes es: ", meses[num_mes-1])