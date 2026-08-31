listaColectivos=[]

def agregar_colectivo():   
    colectivo = {}

    colectivo["linea"] = int(input("Número de línea: "))
    colectivo["interno"] = int(input("Número interno: "))
    colectivo["cantidad_asientos"] = int(input("Cantidad de asientos: "))
    colectivo["asientos_especiales"] = int(input("Asientos especiales: "))
    
    listaColectivos.append(colectivo)
    print("Colectivo agregado correctamente.")


def eliminar_colectivo():
    print("Para eliminar un colectivo se pedirá línea e interno")
    lineaAeliminar = int(input("Ingrese la línea: "))
    internoAeliminar = int(input("Ingrese el interno: "))

    encontrado = False

    for i in range(len(listaColectivos)):
        if (listaColectivos[i]["linea"] == lineaAeliminar and
            listaColectivos[i]["interno"] == internoAeliminar):
            
            listaColectivos.pop(i)
            print("Colectivo eliminado correctamente.")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el colectivo.")


# PROBAR
agregar_colectivo()
eliminar_colectivo()
print(listaColectivos)
