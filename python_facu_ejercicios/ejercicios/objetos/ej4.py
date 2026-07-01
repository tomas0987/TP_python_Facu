class Cuenta:
    def __init__(self, titular, dinero):
        self.titular = titular
        self.dinero = dinero

    def depositar(self):
        monto = int(input("Ingresa el monto a depositar: "))
        self.dinero += monto
        print(f"Depósito exitoso. Saldo actual: {self.dinero}")

    def retirar(self):
        monto = int(input("Ingresa el monto a retirar: "))
        if monto > self.dinero:
            print("Cantidad no disponible")
        else:
            self.dinero -= monto
            print(f"Retiro exitoso. Saldo actual: {self.dinero}")


print("Buenas, ingrese su nombre:")
titular = input("Nombre: ")

# Crear la cuenta con saldo inicial
p = Cuenta(titular, 0)

print(f"Buenas {titular}. ¿Qué operación desea hacer?")

while True:
    decision = int(input("Ingrese 1 para depositar, 2 para retirar, 3 para salir: "))

    if decision == 1:
        p.depositar()
    elif decision == 2:
        p.retirar()
    elif decision == 3:
        print("Gracias por usar el sistema bancario")
        break
    else:
        print("Opción inválida")
