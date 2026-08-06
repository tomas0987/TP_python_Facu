lista_original=[1,3,7,9,10]
print(lista_original)
n=int (input("ingresa un numero para agregar a la lista: "))
if n in lista_original:
    print(f"el numero ya se encuentra en la lista")
else:
    for i in range(len(lista_original)):
        if n < lista_original[i]:
            lista_original.insert(i,n)
            break
    else:
        lista_original.append(n)
print(f"el numero aagregar a la lista es: {n} y la lista final es: {lista_original}")
