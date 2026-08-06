lista_palabras=[]
def borrar(lista_palabras,palabra):
    if palabra=="deshacer":
        if lista_palabras==[]:
            print("la lista ya esta vacia")
        else:
            lista_palabras.pop(-1)
while True:
    print("ingrese salir para salir jeejje")
    palabra=input("ingrese una palabra o ingrese deshacer para borrar: ")
    if palabra=="deshacer":
        borrar(lista_palabras,palabra)    
    elif palabra=="salir":
        break
    else:
        lista_palabras.append(palabra)
for i in lista_palabras:
    print(i,end=" ")