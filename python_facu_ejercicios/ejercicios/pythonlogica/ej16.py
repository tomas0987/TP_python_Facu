lista=[1,2,3,4,2,2]
def eliminar(lista,x):
    if lista==[]:
        return []
    elif lista[0]== x:
        return eliminar(lista[1:],x)
    else:
        return[lista[0]]+eliminar(lista[1:],x)
print(eliminar(lista,2))
