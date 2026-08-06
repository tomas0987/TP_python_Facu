lista_nombres = []

while True:
    nombre = input("Ingrese un nombre para agregar, ingrese 'salir' para finalizar: ")

    if nombre == "salir":
        break

    lista_nombres.append(nombre)

print(f"Listado de jugadores: {lista_nombres}")

# pedir número de pases
try:
    n = int(input("Ingrese un número para la cantidad de pases de la papa: "))
except ValueError:
    print("Debe ser un número natural entero")
    exit()

# calcular quién pierde
if len(lista_nombres) > 0:
    indice = n % len(lista_nombres)
    jugador_perdedor = lista_nombres[indice]
    print(f"La papa explotó, el jugador '{jugador_perdedor}' perdió")
else:
    print("No hay jugadores")
