lista=[1,2,[1,[45]]]

def profundidad(lista):
    if  not isinstance(lista,list):
        return 0
    if lista==[]:
        return 1
    else:
        return 1 + max(profundidad(i)for i in lista)
print(profundidad(lista))