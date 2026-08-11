coladeimpresion=[]

while True:
    orden=input("ingrese el nombre del documento paera mandar a imprimir: ")
    if orden == "terminar":
        break
    else:
        
        coladeimpresion.append(orden)

for i in coladeimpresion:
    n=coladeimpresion.pop(0)
    print(f"imprimiendo: {n}")
    