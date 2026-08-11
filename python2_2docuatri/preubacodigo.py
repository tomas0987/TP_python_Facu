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
    def __init__(self, ladoMaximo:int, cantidad:int):
        self.ladoMaximo = ladoMaximo
        self.cantidad = cantidad
        self.tablero = []
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
        return self.tablero[fila - 1][columna - 1].naufrago

    def distribuirNaufragos(self, cantidad):
        colocados = 0
        while colocados < cantidad:
            fila = random.randint(0, self.ladoMaximo - 1)
            columna = random.randint(0, self.ladoMaximo - 1)

            if not self.tablero[fila][columna].naufrago:
                self.tablero[fila][columna].naufrago = True
                self.tablero[fila][columna].valor = '🏝️'
                colocados += 1


class Sonda:
    def __init__(self, columna, fila):
        self.columna = columna
        self.fila = fila

    def sondear(self, tablero: Tablero):
        # Si hay naufrago en la celda exacta
        if tablero.hayNaufrago(self.fila, self.columna):
            print('Rescataste un naufrago')
            tablero.tablero[self.fila - 1][self.columna - 1].naufrago = False
            return

        # Revisar 8 adyacentes
        posiciones = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        for df, dc in posiciones:
            nf = self.fila - 1 + df
            nc = self.columna - 1 + dc

            if 0 <= nf < tablero.ladoMaximo and 0 <= nc < tablero.ladoMaximo:
                if tablero.tablero[nf][nc].naufrago:
                    print("Hay un naufrago alrededor")
                    return

        print("No hay naufragos cerca")

    def activar(self, tablero: Tablero):
        self.sondear(tablero)
        tablero.actualizarCelda(self.fila, self.columna, '🚨')

    def __str__(self):
        return f'\nSonda 🚨 desplegada en columna {self.columna}, fila {self.fila}\n'


class Naufrago:
    @staticmethod
    def PosicionValida(columna: int, fila: int, tablero: Tablero):
        posiciones = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        for df, dc in posiciones:
            nf = fila + df
            nc = columna + dc

            if 0 <= nf < tablero.ladoMaximo and 0 <= nc < tablero.ladoMaximo:
                if tablero.tablero[nf][nc].naufrago:
                    return True
        return False


def naufrago(dificultad):

    match dificultad:
        case 'facil':
            intentos = 10
            ladoMaximo = 6
            cantidadNaufragos = 4
        case 'intermedio':
            intentos = 15
            ladoMaximo = 8
            cantidadNaufragos = 8
        case 'dificil':
            intentos = 20
            ladoMaximo = 10
            cantidadNaufragos = 11

    tablero = Tablero(ladoMaximo, cantidadNaufragos)

    while intentos > 0:
        tablero.mostrar()
        print(f"\nTenes {intentos} intentos.")

        # Entrada columna
        while True:
            try:
                columna = int(input("Ingrese su numero de columna: "))
                if 1 <= columna <= ladoMaximo:
                    break
                print("Fuera de mapa.")
            except ValueError:
                print("Solo números.")

        # Entrada fila
        while True:
            try:
                fila = int(input("Ingrese su numero de fila: "))
                if 1 <= fila <= ladoMaximo:
                    break
                print("Fuera de mapa.")
            except ValueError:
                print("Solo números.")

        sonda = Sonda(columna, fila)
        print(sonda)
        sonda.activar(tablero)

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

    dificultad = input("Ingrese su dificultad: ").lower()

    if dificultad == 'q':
        break
    if dificultad not in ('facil', 'intermedio', 'dificil'):
        print("Ingrese una opcion valida.")
    else:
        naufrago(dificultad)
