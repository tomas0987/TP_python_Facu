lista=[1,2,3,4,5]
def invertirLista(lista):
    if len(lista)<=1:
        return lista
    else:
        return invertirLista(lista[1:])+[lista[0]]
print(invertirLista(lista))