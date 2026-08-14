listaNombres=[]

while True:
    n=input(f"ingrese su nombre: ")
    if n =="terminar":
        break
    listaNombres.append(n)

while True:
    opcion=input(f"ingrese enter para pasar al siguien turno:")
    if opcion=="":
        m=listaNombres.pop(0)
        print(m)
    if listaNombres==[]:
        break
    