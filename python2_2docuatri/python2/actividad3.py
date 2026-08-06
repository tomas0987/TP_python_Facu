lista1=[2,1,4,3,5]
lista2=[7,8,10,6,9]

def estaordenada(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

def ordenar(lista):
    if estaordenada(lista):
        return lista
    else:
        for i in range (len(lista)-1):
            if lista[i]> lista[i+1]:
                  lista[i], lista[i+1] = lista[i+1], lista[i]
        return ordenar(lista)  
estaordenada(lista1)
estaordenada(lista2)            
ordenar(lista1)
ordenar(lista2)             
print(lista1)
print(lista2)
lista3=[]
n=0
vuelta=0
while len(lista3) == 0 or lista3[-1] != lista2[-1]:

    if n==0 :
        lista3.append(lista1[vuelta])
        n=1
    else:
        if n==1:
            lista3.append(lista2[vuelta])
            n=0
            vuelta+=1
print(lista3)