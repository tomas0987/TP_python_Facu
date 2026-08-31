import random

class SensorTermico:
    
    def __init__(self, id_sensor: str, ubicacion: str, temperaturas: list[float]):
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.__temperaturas = temperaturas

    @property
    def temperaturas(self):
        return self.__temperaturas.copy()

    def actualizar_temperaturas(self):
        numero = random.randint(0, 85)
        self.__temperaturas.append(numero)
        return numero

    def mostrar_lista(self):
        copia = self.temperaturas
        print(copia)

    def verificar_temperaturas(self, numero):
        if 0 <= numero <= 85:
            print("Temperatura en rango válido y normal")
        else:
            print("Temperatura fuera de lo normal")


sensortermico = SensorTermico(1, "Rack-A1", [])

while True:
    opcion = int(input("Ingrese la opción: 1- actualizar temperatura  2- mostrar lista  3- salir: "))

    if opcion == 1:
        numero = sensortermico.actualizar_temperaturas()
        sensortermico.verificar_temperaturas(numero)

    elif opcion == 2:
        sensortermico.mostrar_lista()

    else:
        break
