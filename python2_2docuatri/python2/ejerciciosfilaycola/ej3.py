lista = []
vuelta = []

texto = input("Ingrese una palabra: ")

for i in texto:
    lista.append(i)

while lista:
    vuelta.append(lista.pop())   # saca el último y lo agrega

print("Original:", texto)
print("Invertida:", "".join(vuelta))
