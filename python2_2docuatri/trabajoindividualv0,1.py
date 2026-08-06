import random

# ---------------- MATRIZ OCULTA ----------------

def crearmatriz():
    matriz = [[0 for _ in range(6)] for _ in range(6)]
    
    posiciones = random.sample(range(36), 4)
    for pos in posiciones:
        fila = pos // 6
        columna = pos % 6
        matriz[fila][columna] = 1
    return matriz

oculta = crearmatriz()

# ---------------- MATRIZ VISIBLE ----------------

def matrizusuario():
    return [["🌊" for _ in range(6)] for _ in range(6)]

def mostrarmatrizusuario(matriz):
    for fila in matriz:
        print(" ".join(fila))

visible = matrizusuario()

# ---------------- RADAR ----------------
radares = 20

def radar(fila, col):
    global radares
    radares -= 1

    señales = 0

    posiciones = [
        (fila - 1, col),  # arriba
        (fila + 1, col),  # abajo
        (fila, col - 1),  # izquierda
        (fila, col + 1)   # derecha
    ]

    for f, c in posiciones:
        if 0 <= f < 6 and 0 <= c < 6:
            if oculta[f][c] == 1:
                señales += 1

    return señales

# ---------------- RESCATE ----------------

def rescatar(fila, col):
    if oculta[fila][col] == 1:
        oculta[fila][col] = 0
        visible[fila][col] = "🧍"
        print("¡Rescataste un náufrago!")
    else:
        visible[fila][col] = "❌"
        print("No había ningún náufrago aquí.")

# ---------------- CHEQUEOS ----------------

listanorepeticion = []

def repe(lista, tupla):
    return tupla in lista

def chequearCelda(fila, col):
    if 0 <= fila < 6 and 0 <= col < 6:
        if oculta[fila][col] == 0:
            visible[fila][col] = "🛜"
        else:
            visible[fila][col] = "🧍"

def chequearAdyacentes(fila, col):
    chequearCelda(fila + 1, col)
    chequearCelda(fila - 1, col)
    chequearCelda(fila, col + 1)
    chequearCelda(fila, col - 1)

# ---------------- JUEGO ----------------

while True:
    mostrarmatrizusuario(visible)

    print("\nOpciones:")
    print("1 - Radar")
    print("2 - Rescatar")
    print("3 - Salir")
    print(f"Radares restantes: {radares}📡")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        if radares > 0:
            fila = input("Fila (0-5): ")
            col = input("Columna (0-5): ")

            if not fila.isdigit() or not col.isdigit():
                print("Debés ingresar números enteros.")
                continue

            fila = int(fila)
            col = int(col)

            if not (0 <= fila < 6 and 0 <= col < 6):
                print("Coordenadas fuera del rango.")
                continue

            if repe(listanorepeticion, (fila, col)):
                print("La casilla ya fue elegida.")
                continue

            listanorepeticion.append((fila, col))

            señales = radar(fila, col)
            visible[fila][col] = "📡"

            chequearAdyacentes(fila, col)

            if señales > 0:
                print(f"📡 Se detectaron {señales} náufragos alrededor.")
            else:
                print("📡 No se detectó nada alrededor.")
        else:
            print("No tenés más radares.")

    elif opcion == "2":
        fila = input("Fila (0-5): ")
        col = input("Columna (0-5): ")

        if not fila.isdigit() or not col.isdigit():
            print("Debés ingresar números enteros.")
            continue

        fila = int(fila)
        col = int(col)

        if not (0 <= fila < 6 and 0 <= col < 6):
            print("Coordenadas fuera del rango.")
            continue

        if repe(listanorepeticion, (fila, col)):
            print("La casilla ya fue elegida.")
            continue

        listanorepeticion.append((fila, col))
        rescatar(fila, col)

    elif opcion == "3":
        break

    else:
        print("Opción inválida.")
