coladeimpresion=[]

while True:
    orden=input("ingrese el nombre del documento para mandar a imprimir: ")
    if orden == "terminar":
        break
    coladeimpresion.append(orden)

while coladeimpresion:
    i = coladeimpresion.pop(0)
    print(f"imprimiendo: {i}")
