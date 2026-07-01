
lista=[1,2,3,4,5]
i=0
def maxnum(lista,i):
    if lista[i]>=(lista[i+1]):
        return lista[i]
    
    else:
        i+=1
        return (maxnum(lista[i]))
print(maxnum(lista,i))