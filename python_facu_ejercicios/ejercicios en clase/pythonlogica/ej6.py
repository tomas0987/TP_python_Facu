lista=[1,2,3,4,5]
def sumaValores(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+sumaValores(lista[1:])
print(f"los valores son: {sumaValores(lista)}")   