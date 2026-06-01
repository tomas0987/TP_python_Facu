
with open("frases.txt","r",encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

contador = contenido.count("python")

print(f"La palabra 'python' aparece {contador} veces")

