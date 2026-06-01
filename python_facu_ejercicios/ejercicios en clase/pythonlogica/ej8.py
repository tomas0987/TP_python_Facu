
lista=[1,2,3,4,5]

def maxnum(lista):
    if lista[0]== max(lista):
        return 0
    else:
        return (maxnum(lista[1:])*0) + max(lista)
print(maxnum(lista))