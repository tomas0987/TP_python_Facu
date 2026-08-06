# Listas de trenes por línea
linea_SanMartin = ["011", "012", "013", "014"]
linea_Urquiza   = ["017", "002", "015", "014", "001", "004", "005"]
linea_MitreA    = ["018", "028", "058", "048", "089", "009", "005"]
linea_MitreB    = ["018", "028", "058", "048", "089"]

# Función para mostrar cada línea con formato de título + listado
def mostrar_linea(nombre, lista):
    print(f"\n{nombre}")
    print("-" * len(nombre))
    for tren in lista:
        print(f"  • {tren}")

# Mostrar todas las líneas
mostrar_linea("Línea San Martín", linea_SanMartin)
mostrar_linea("Línea Urquiza", linea_Urquiza)
mostrar_linea("Línea Mitre A", linea_MitreA)
mostrar_linea("Línea Mitre B", linea_MitreB)

# Crear lista con trenes usados en más de una línea
todas = linea_SanMartin + linea_Urquiza + linea_MitreA + linea_MitreB
repetidos = []

for tren in todas:
    if todas.count(tren) > 1 and tren not in repetidos:
        repetidos.append(tren)

# Mostrar trenes repetidos
print("\nTrenes usados en más de una línea:")
print("----------------------------------")
for t in repetidos:
    print("  •", t)
