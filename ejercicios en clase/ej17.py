suma=0
contador=0
while suma<24:
    num=int(input("ingrese el numero que saco: "))
    if num <1 or num >6:
        print("el numero ingresado no es valido, por favor ingrese un numero entre 1 y 6")
    else:
        suma= suma+num
        contador+= 1
print("la suma de los numeros ingresados es: ", suma, "usted ha ganado el juego") 
print("la cantidad de numeros ingresados es: ", contador) 