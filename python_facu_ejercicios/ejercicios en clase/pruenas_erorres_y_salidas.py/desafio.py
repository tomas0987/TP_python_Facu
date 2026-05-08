#calcula las comisiones
from operator import index


def calcular_comision(monto, categoria):
    if categoria == "a":
        return monto * 0.10
    elif categoria == "b":
        return monto * 0.15 
    elif categoria == "c":
        return monto * 0.20
    
aux=1
#listas para almacenar los datos de los vendedores
legajo_vendedores = []
monto_ventas= []
comisiones = []
categorias=[]


while aux==1:
    #se ingrsean los datos del vendedor
    legajo= int(input("ingrse el legajo del vendedor: "))
    legajo_vendedores.append(legajo)
    
    #monto de ventas
    monto= int(input("ingrese el monto de ventas: "))
    monto_ventas.append(monto)
    
    #categoria del vendedor
    cat = input("Ingrese la categoria del vendedor (A/B/C): ").lower()

    while cat not in ("a", "b", "c"):
        print("Categoría no válida")
        cat = input("Ingrese la categoria del vendedor (A/B/C): ").lower()
    
    categorias.append(cat)
        
    #se calcula la comision y se agrega a la lista de comisiones
    comision = calcular_comision(monto, cat)
    comisiones.append(comision)
    
#te pregunta si deseas continuar o no
    rompe=str(input("desea agregar otro vendedor? (si/no): "))
    if rompe == "no":
        break
    else:
        aux=1
        
# muestra los datos ingresados
print(f"legajo del vendedor: {legajo_vendedores}")
print(f"monto de ventas: {monto_ventas}")
print(f"comisiones: {comisiones}")
print(f"categoria del vendedor: {categorias}")


#suma total de las comisiones
total_comisiones = sum(comisiones)
print(f"total de comisiones: {total_comisiones}")

#muestra el mayor legajo con el mayor monto de ventas
max_monto= max(monto_ventas)
indice_max = monto_ventas.index(max_monto)
print(f"el legajo con el mayor monto de ventas es: {legajo_vendedores[indice_max]}, con un monto de ventas de: {max_monto}")                    