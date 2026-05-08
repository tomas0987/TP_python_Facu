lista=["tomas","juan","maria","ana"]
print(lista[-1])
print(type(lista))
def funcion(nombre):
    nombre= input("ingrese un nombre: ")
    nombre= nombre.capitalize()
    lista.append(nombre)
    lista.sort(key=str.lower)
    print(f"hola {nombre}, bienvenido a python")
    print(lista)
   
    
funcion("nombre")