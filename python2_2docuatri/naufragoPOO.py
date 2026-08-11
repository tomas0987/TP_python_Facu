import time
import random

class Celda:

    def __init__(self, columna:int, fila:int, valor:str, naufrago:bool = False):
        self.columna = columna
        self.fila = fila
        self.valor = valor
        self.naufrago = naufrago

    def __str__(self):
        return f'{self.valor}'
class Tablero:
    def __init__(self, ladoMaximo:int,cantidad:int):
        self.ladoMaximo = ladoMaximo
        self.tablero = []
        self.cantidad=cantidad
        self.crear()
        

    def crear(self):
        self.tablero = [
            [Celda(columna, fila, '🌊') for columna in range(self.ladoMaximo)]
            for fila in range(self.ladoMaximo)
            ]
        
        self.distribuirNaufragos(self.cantidad)

    def mostrar(self):
        numeros = "   " + " ".join(f"{columna:2d}" for columna in range(1, self.ladoMaximo + 1))
        print(numeros)

        for indice, fila in enumerate(self.tablero, start=1):
            mapa_fila = " ".join(str(celda) for celda in fila)
            print(f"{indice:2d} {mapa_fila}")

    def actualizarCelda(self, fila:int, columna:int, valor:str):
        self.tablero[fila - 1][columna - 1].valor = valor

    def hayNaufrago(self, fila:int, columna:int):
        return self.tablero[fila -1][columna-1].naufrago

    def distribuirNaufragos(self, cantidad):
        colocados = 0
        Naufrago.PosicionValida(columna,fila,self.tablero,self.hayNaufrago)
        while colocados < cantidad:
            fila = random.randint(0, self.ladoMaximo - 1)
            columna = random.randint(0, self.ladoMaximo - 1)

            if not self.tablero[fila][columna].naufrago:
                self.tablero[fila][columna].naufrago = True
                self.tablero[fila][columna].valor = '🏝️ '
                colocados += 1

class Sonda:
    def __init__(self, columna, fila):
        self.columna = columna
        self.fila = fila

    def sondear(self, tablero: Tablero):
        if tablero.hayNaufrago(self.fila, self.columna):
            print('Rescataste un naufrago')
            tablero.tablero[self.fila - 1][self.columna - 1].naufrago = False

        for i in range(tablero.ladoMaximo):
            if tablero.tablero[self.fila - 1][i].naufrago:
                print('Hay un naufrago alrededor')
                return

        for i in range(tablero.ladoMaximo):
            if tablero.tablero[i][self.columna -1].naufrago:
                print('Hay un naufrago alrededor')
                return

    def activar(self,tablero: Tablero):
        self.sondear(tablero)
        tablero.actualizarCelda(self.fila, self.columna, '🚨')

    def __str__(self):
        return f'\nSonda 🚨 desplegada en {self.columna}, {self.fila}\n'
                

class Naufrago:
    def __init__(self, fila: int, columna: int, rescatado: bool = False):
        self.fila = fila
        self.columna = columna
        self.rescatado = rescatado

    def PosicionValida(self, columna: int, fila: int, tablero: Tablero, haynaufrago: bool = False):
        posiciones = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        for delta_fila, delta_columna in posiciones:
            fila_vecina = fila + delta_fila
            columna_vecina = columna + delta_columna

            if 0 <= fila_vecina < tablero.ladoMaximo and 0 <= columna_vecina < tablero.ladoMaximo:
                celda = tablero.tablero[fila_vecina][columna_vecina]
                if celda.naufrago:
                    return True

        return False

def naufrago(dificultad):            

    match dificultad:
        case 'facil':
            intentos = 10
            ladoMaximo = 6
            cantidadNaufragos=4
        case 'intermedio':
            intentos = 15
            ladoMaximo = 8
            cantidadNaufragos=8
        case 'dificil':
            intentos = 20
            ladoMaximo = 10
            cantidadNaufragos=11
    encontro = False

    tablero = Tablero(ladoMaximo,cantidadNaufragos)


    while intentos > 0:
        tablero.mostrar()

        print(f"\nTenes {intentos} intentos.")

        while True:                                                         # Encontrar manera de no repetir

            try:
                columna = int(input("Ingrese su numero de columna: "))

                if columna < 1 or columna > ladoMaximo:
                    print(f"Fuera de mapa. Matriz de {ladoMaximo}x{ladoMaximo}")
                else:
                    break

            except ValueError:
                print("\nSolo valores numericos (numeros).\n")

        while True:                                                         # Encontrar manera de no repetir

            try:
                fila = int(input("Ingrese su numero de fila: "))

                if fila < 1 or fila > ladoMaximo:
                    print(f"Fuera de mapa. Matriz de {ladoMaximo}x{ladoMaximo}")
                else:
                    break

            except ValueError:
                print("\nSolo valores numericos (numeros).\n")

        sonda = Sonda(columna, fila)

        print(sonda)
        sonda.activar(tablero)

        if encontro == True:
            print("Encontraste al naufrago.")
            break
        else:
            intentos -= 1
            time.sleep(1)

while True:
    print("""
-----------------------
    NAUFRAGO!!!!1!
-----------------------

- Facil
- Intermedio
- Dificil

q. Salir
""")

    dificultad = str(input("Ingrese su dificultad: ")).lower()

    if dificultad == 'q':
        break
    if dificultad not in ('facil','intermedio','dificil'):
        print("\nIngrese una opcion valida.")
    else:

        naufrago(dificultad)