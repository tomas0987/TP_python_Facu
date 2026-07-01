palabra=list("argentina")
def contarelementos(palabra):
    if palabra == []:          
        return 0
    else:
        return 1 + contarelementos(palabra[1:])

print(contarelementos(palabra))