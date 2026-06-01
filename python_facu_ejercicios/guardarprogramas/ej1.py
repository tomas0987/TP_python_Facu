alumnos_lista=[]
while True:
    nombres=input("ingrese el nombre del alumno:").capitalize()
    if nombres == "Fin":
        break
    alumnos_lista.append(nombres)

with open("archivo_alumnos.txt","w",encoding="utf-8") as archivo:
    for i, nombres in enumerate(alumnos_lista, start=1):
        archivo.write(f"{i}.{nombres}\n")

print("\nLos nombres de los alumnos fueron guardados en:'archivo_alumnos.txt'")
with open("archivo_alumnos.txt","r",encoding="utf-8")as archivo:
    lineas=archivo.read()
    print(lineas)
        