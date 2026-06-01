with open("variasfrases.txt","r",encoding="utf-8")as texto:
    print("esta es la primer linea",)
    print(texto.readline(),"\n")
    resto=texto.read()
    print("esto es el resto del texto")
    print(resto,"\n")
    texto.seek(0)#esto es como un carriage return pero al comienzo del texto
    print("se imprime todo el texto")
    print(texto.read())
    