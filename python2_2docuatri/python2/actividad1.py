import random
n= int(input("ingresa una canridad maxima de numero para la lista"))
m= int(input("ingresa ota cantidad para la lista de nuemeroo a eliminar"))
lista1= [random.randint(1,10) for _ in range (n)]
lista2=[random.randint(1,10)for _ in range (m)]
def eliminarelementos(lista1,lista2):
    return[x for x in lista1 if x not in lista2]
eliminarelementos(lista1,lista2)
print(f"lista orginal {lista1}")
print(f"lista con los valores a eliminar {lista2}")
resultado= eliminarelementos(lista1,lista2)
print(f"lista resultante = {resultado}")