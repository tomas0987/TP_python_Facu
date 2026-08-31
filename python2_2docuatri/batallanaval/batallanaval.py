# -*- coding: utf-8 -*-

import random

# ------------------------------
# FUNCIONES AUXILIARES
# ------------------------------

def leer_entero(prompt, minimo, maximo):
    while True:
        try:
            valor = int(input(prompt))
            if minimo <= valor <= maximo:
                return valor
            print(f"Debe ingresar un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


# ------------------------------
# OPCIONES DEL TABLERO
# ------------------------------

def OpcionesTablero():
    print("Elegí el tamaño del tablero:")
    print("1) 8x8")
    print("2) 10x10")
    print("3) 12x12")
    print("A mayor tamaño, más barcos disponibles!!!")

    opcion = leer_entero("Ingrese su opción: ", 1, 3)

    if opcion == 1:
        return 8, 8, opcion
    elif opcion == 2:
        return 10, 10, opcion
    return 12, 12, opcion


# ------------------------------
# CLASE TABLERO
# ------------------------------

class TABLERO:

    def __init__(self, filas, columnas, visible=False):
        self.filas = filas
        self.columnas = columnas
        self.visible = visible
        self.matriz = [["🌊" for _ in range(columnas)] for _ in range(filas)]

    def mostrar(self):
        for fila in self.matriz:
            if self.visible:
                print(*fila)
            else:
                oculto = [cel if cel == "🌊" else "🌊" for cel in fila]
                print(*oculto)

    def colocar_barco(self, fila, columna, tamaño, orientacion, simbolo=None):
        posiciones = []

        if simbolo is None:
            simbolo = "⛵" if tamaño == 2 else "🚤" if tamaño == 3 else "🚢"

        for i in range(tamaño):
            if orientacion == 1:  # izquierda
                f, c = fila, columna - i
            elif orientacion == 2:  # derecha
                f, c = fila, columna + i
            elif orientacion == 3:  # arriba
                f, c = fila - i, columna
            else:  # abajo
                f, c = fila + i, columna

            if f < 0 or f >= self.filas or c < 0 or c >= self.columnas:
                return False

            if self.matriz[f][c] != "🌊":
                return False

            posiciones.append((f, c))

        for f, c in posiciones:
            self.matriz[f][c] = simbolo

        return True


# ------------------------------
# OPCIONES DE BARCOS
# ------------------------------

def OpcionesBarcosU(opcion):
    print("Hay 3 tipos de barcos:")
    print("1) ⛵⛵ (tamaño 2)")
    print("2) 🚤🚤🚤 (tamaño 3)")
    print("3) 🚢🚢🚢🚢 (tamaño 4)")

    if opcion == 1:
        print("Tablero 8x8 → 3 barcos tipo 1, 2 tipo 2, 1 tipo 3.")
    elif opcion == 2:
        print("Tablero 10x10 → 5 barcos tipo 1, 3 tipo 2, 2 tipo 3.")
    else:
        print("Tablero 12x12 → 7 barcos tipo 1, 4 tipo 2, 3 tipo 3.")


def obtener_orientacion():
    print("Ingrese el sentido para colocar el barco:")
    print("1) izquierda")
    print("2) derecha")
    print("3) arriba")
    print("4) abajo")
    return leer_entero("Opción: ", 1, 4)


# ------------------------------
# COLOCAR BARCOS USUARIO
# ------------------------------

def colocar_barco_usuario(tablero, tipo_barco):
    tamaños = {1: 2, 2: 3, 3: 4}
    tamaño = tamaños[tipo_barco]

    while True:
        print(f"Colocando barco tipo {tipo_barco} de tamaño {tamaño}.")
        fila = leer_entero("Fila: ", 1, tablero.filas) - 1
        columna = leer_entero("Columna: ", 1, tablero.columnas) - 1
        orientacion = obtener_orientacion()

        if tablero.colocar_barco(fila, columna, tamaño, orientacion):
            tablero.mostrar()
            return

        print("No se puede colocar el barco en esa posición. Intente otra vez.")


def DistribuirBarcosU(tablero, opcion):
    OpcionesBarcosU(opcion)

    cantidades = {
        1: {1: 3, 2: 2, 3: 1},
        2: {1: 5, 2: 3, 3: 2},
        3: {1: 7, 2: 4, 3: 3},
    }

    tipos = cantidades[opcion]

    for tipo, cantidad in tipos.items():
        for i in range(cantidad):
            print(f"\nBarco {i + 1} de {cantidad} del tipo {tipo}.")
            colocar_barco_usuario(tablero, tipo)


# ------------------------------
# COLOCAR BARCOS MÁQUINA
# ------------------------------

def colocar_barcos_aleatorios(tablero, opcion):
    cantidades = {
        1: {1: 3, 2: 2, 3: 1},
        2: {1: 5, 2: 3, 3: 2},
        3: {1: 7, 2: 4, 3: 3},
    }

    tipos = cantidades[opcion]

    for tipo, cantidad in tipos.items():
        tamaño = {1: 2, 2: 3, 3: 4}[tipo]
        simbolos = {1: "⛵", 2: "🚤", 3: "🚢"}

        for _ in range(cantidad):
            colocado = False
            while not colocado:
                fila = random.randrange(tablero.filas)
                columna = random.randrange(tablero.columnas)
                orientacion = random.randint(1, 4)
                colocado = tablero.colocar_barco(fila, columna, tamaño, orientacion, simbolo=simbolos[tipo])


# ------------------------------
# BOMBA
# ------------------------------

def colocarBomba(tablero):
    print("\n--- TU TURNO: LANZAR BOMBA ---")
    fila = leer_entero("Fila: ", 1, tablero.filas) - 1
    columna = leer_entero("Columna: ", 1, tablero.columnas) - 1

    if tablero.matriz[fila][columna] != "🌊":
        print("🔥 ¡has derribado una parte de un barco!")
        tablero.matriz[fila][columna] = "💣"
    else:
        print("🌊 la bomba no ha impactado.")

    return fila, columna


# ------------------------------
# INICIO DEL JUEGO
# ------------------------------

filas, columnas, opcion = OpcionesTablero()

tablero_usuario_visible = TABLERO(filas, columnas, visible=True)
tablero_maquina_oculto = TABLERO(filas, columnas, visible=False)

print("\nTu tablero:")
tablero_usuario_visible.mostrar()

print("\n--- COLOCACIÓN DE BARCOS DEL USUARIO ---")
DistribuirBarcosU(tablero_usuario_visible, opcion)

print("\n--- COLOCACIÓN DE BARCOS DE LA MÁQUINA ---")
colocar_barcos_aleatorios(tablero_maquina_oculto, opcion)

print("\nTablero del usuario listo:")
tablero_usuario_visible.mostrar()

print("\nTablero de la máquina (oculto):")
tablero_maquina_oculto.mostrar()

# Turno del usuario
fila, columna = colocarBomba(tablero_maquina_oculto)

print("\nTablero de la máquina actualizado (oculto):")
tablero_maquina_oculto.mostrar()
