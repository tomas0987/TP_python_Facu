# la idea es hacer una funcion a la que se le de una palabra y devuelva las vocales y cuantas tiene
vocales=["a","e","i","o","u"]
palabra=input("ingrese la palabra que desea evaluar: ").lower()

def contarvocales(vocales,palabra):
    contador=0
    for i in palabra:
        if i in vocales:
            contador+=1
    return contador
print(contarvocales(vocales,palabra))
