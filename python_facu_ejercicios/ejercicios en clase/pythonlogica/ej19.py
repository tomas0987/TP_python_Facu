lista = [1, [2, 3]]

def suma(lista):
    sumaTotal = 0
    for elem in lista:
        if isinstance(elem, list):
            sumaTotal += suma(elem)
        else:
            sumaTotal += elem
    return sumaTotal

print(suma(lista))
