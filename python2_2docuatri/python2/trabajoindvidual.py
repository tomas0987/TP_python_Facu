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
radares=20
def radar(num):
    global radares
    radares-=1
    fila = num // 6
    col = num % 6

    señales = 0

    # posiciones a revisar
    posiciones = [
        num - 1,  # izquierda
        num + 1,  # derecha
        num - 6,  # arriba
        num + 6   # abajo
    ]

    for p in posiciones:
        if 0 <= p < 36:  # dentro del tablero
            f = p // 6
            c = p % 6
            if oculta[f][c] == 1:
                señales += 1
  
    
        
    return señales

# ---------------- RESCATE ----------------

def rescatar(num):
    fila = num // 6
    col = num % 6

    if oculta[fila][col] == 1:
        oculta[fila][col] = 0
        visible[fila][col] = "🧍"
        print("¡Rescataste un náufrago!")
    else:
        visible[fila][col] = "❌"
        print("No había ningún náufrago aquí.")

# ---------------- JUEGO ----------------
listanorepeticion = []


def repe(lista, num):
    return num in lista

def chequearCelda(fila,col):
    if 0<= fila < 6 and 0 <= col <6:
        if oculta[fila][col] == 0:
            visible[fila][col] = "🛜 "
        else:
            visible[fila][col] = "🧍"

def chequearAdyacentes(fila,col):
    chequearCelda(fila + 1, col)
    chequearCelda(fila - 1, col)
    chequearCelda(fila, col + 1)
    chequearCelda(fila, col - 1)

while True:
    mostrarmatrizusuario(visible)

    print("\nOpciones:")
    print("1 - Radar")
    print("2 - Rescatar")
    print("3 - Salir")
    print(f" radares restantes: {radares}📡")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        if radares > 0:
            entrada = input("Ingresá un número del 0 al 35: ")
            if not entrada.isdigit():
                print("Se debe ingresar un número entero, no una letra.")
                continue
            num = int(entrada)
            if not 0 <= num <= 35:
                print("El número debe estar entre 0 y 35.")
                continue
            if repe(listanorepeticion, num):
                print("la casilla ya fue elegida")
                continue
            listanorepeticion.append(num)
            señales = radar(num)

            fila = num // 6
            col = num % 6
            visible[fila][col] = "📡"

            chequearAdyacentes(fila,col)
            
            if señales > 0:
                print(f"📡 Se detectaron {señales} náufragos alrededor.")
            else:
                print("📡 No se detectó nada alrededor.")
        else:
            print("no tienes mas radares")
    elif opcion == "2":
        entrada = input("Ingresá un número del 0 al 35: ")
        if not entrada.isdigit():
            print("Se debe ingresar un número entero, no una letra.")
            continue
        num = int(entrada)
        if not 0 <= num <= 35:
            print("El número debe estar entre 0 y 35.")
            continue
        if repe(listanorepeticion, num):
            print("la casilla ya fue elegida")
            continue
        listanorepeticion.append(num)
        rescatar(num)
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
