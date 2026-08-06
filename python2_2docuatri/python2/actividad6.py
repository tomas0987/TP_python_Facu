import random

def ListaDeItems():
    alfabeto= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lista=[]
    largolista=random.randint(5,10)
    for x in range(0,largolista):
        lista.append(random.choice(alfabeto))
    return lista

lista1= ListaDeItems()

lista2= ListaDeItems()

print(lista1,lista2)

lista3 = []

for j in lista2:
    if j in lista1 and j not in lista3:
        lista3.append(j)

print(lista3)
