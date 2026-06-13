lista=[1,2,3]
def productelement(lista):
    if lista==[]:
        return 1
    else:
        return lista[0]* productelement(lista[1:])
print(productelement(lista))