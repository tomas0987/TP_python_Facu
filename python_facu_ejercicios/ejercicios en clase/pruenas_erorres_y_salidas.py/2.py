datos = [10,20,30,40,50]
resultado = 0
for i in range(0, len(datos), 2):
    if datos[i] % 10 == 0:
        resultado += datos[i]
print(resultado)
