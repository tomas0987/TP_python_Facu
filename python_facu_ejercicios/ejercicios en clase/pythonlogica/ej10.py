num=12345

def sumadigitos(num):
    suma = 0
    for i in str(num):
        suma += int(i)
    return suma

print(sumadigitos(num))
