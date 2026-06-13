lista=[1,2,3,4,5]
def orden(lista):
    if lista==[]:
        return True
    elif len(lista)==1:
        return True
    elif lista[0]>lista[1]:
        return False
    return orden (lista[1:])
print(orden(lista))
        