from operator import index

lista=["pelota","milanesa","programacion","plumas"]

def contarElementos(lista):
    if not lista:
        return 0
    else:
        return 1 + contarElementos(lista[1:])
print(contarElementos(lista))