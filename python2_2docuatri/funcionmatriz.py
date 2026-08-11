def CrearMatriz(filas,columnas):
    matriz=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
          fila.append("🌊")  
        matriz.append(fila)
    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        print("".join(str(valor)for valor in fila))   
