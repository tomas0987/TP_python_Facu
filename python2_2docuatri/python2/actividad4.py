lista_nombres = []
palabra = "FIN"

while True:
    nombre = input("Ingrese el nombre del alumno: ").upper()
    lista_nombres.append(nombre)

    terminar = input("Ingrese FIN para finalizar: ").upper()
    if terminar == "FIN":
        break

lista_nombres.sort()

print("LISTA DE ALUMNOS:")
for i, nombre in enumerate(lista_nombres, start=1):
    print(f"{i:02d} {nombre}")
