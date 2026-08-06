lista=[]
paginas=["Google.com","YouTube.com","Amazon.com","Facebook.com"]
def avanzar(lista,paginas,opcion):
    print(f"has ingresado a {paginas[opcion-1]}")
    lista.append(paginas[opcion-1])
def retroceder(lista,paginas,opcion):
    if len(lista)<=1:
        print("ya estas en el home de navegador")
        return
    print(f"has retrocedido a {lista[-2]}")
    lista.pop(-1)  
while True:
    try:
        print(f"Ingrese la opcion de la pagina a la que desea ingresar: \n 1-Google \n 2- You Tube \n 3- Amazon \n 4- Facebook \n 5- retroceder")
        print (lista)
        opcion= int(input("ingrese la opcion: "))
        if opcion != 5:
            
            avanzar(lista,paginas,opcion)
        else:
            
           retroceder(lista,paginas,opcion) 
        
    except ValueError:
        print("no tenes que poner letritas mostro")
