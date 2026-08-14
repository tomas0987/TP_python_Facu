filanumero=[]
filapedido=[]
while True:
    try:
        opcion=int(input(f"ingresa 1) para agregar un pedido, 2) para retirar el pedido: "))
        if opcion == 1:
            opcion2=input(f"ingrese nombre del cliente: ")
            filanumero.append(opcion2)
        elif opcion==2:
            filapedido.append(filanumero.pop(0))
            if filapedido==[]  and filanumero==[]:
                break
            print(filapedido.pop(0))
    except ValueError:
        print("ingrese una de la sopciones disponibles")