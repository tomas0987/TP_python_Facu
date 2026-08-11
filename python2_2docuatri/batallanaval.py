from funcionmatriz import CrearMatriz,imprimirMatriz

print(f"Hola, bienvenido al juego de batalla naval\n ".center(100) )
print("\n\n")
#creacion de tablero
print(f"para comenzar ingrese la cantidad de filas y columnas para el tablero")
try:
    columnas=int(input("ingrese la cantidad de columnas: "))
    filas=int(input("ingrese la cantidad de filas: "))
except ValueError:
    print("ingrese un numero entero")
matriz=CrearMatriz(filas,columnas)
imprimirMatriz(matriz)

