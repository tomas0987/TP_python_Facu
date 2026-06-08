#codigo comentado por IA
# Clase que representa una poción
class Potion:
    def __init__(self, nombre, cant, tipo, efecto):
        self.nombre = nombre      # Nombre de la poción
        self.cant = cant          # Cantidad de usos que tiene
        self.tipo = tipo          # Tipo: curativa, fortaleza, etc.
        self.efecto = efecto      # Valor del efecto (curación o multiplicador)

    # Método para aplicar la poción a un objetivo (player, enemigo, etc.)
    def aplicar(self, target):
        if self.cant <= 0:
            print("No te quedan más pociones")
            return
        
        # Si la poción cura vida
        if self.tipo == "curativa":
            target._life += self.efecto

            # Límite máximo de vida (400 en tu caso)
            if target._life > 400:
                target._life = 400

            print(f"{target.name} recuperó vida. Vida actual: {target._life}")

        # Si la poción aumenta el daño
        elif self.tipo == "fortaleza":
            target.damage *= self.efecto   # Multiplica el daño
            print(f"{target.name} aumentó su fuerza. Daño actual: {target.damage}")

        # Se consume un uso de la poción
        self.cant -= 1


# Clase que representa un personaje
class Character:
    
    def __init__(self, life, damage, name):
        self.name = name      # Nombre del personaje
        self._life = life     # Vida del personaje
        self.damage = damage  # Daño base del personaje
        
    # Método para atacar a otro personaje
    def attack(self, target):
        print(f"{self.name} ha atacado a {target.name} y causó {self.damage} de daño")
        target.receive_damage(self.damage)   # El objetivo recibe daño
        
    # Método para recibir daño
    def receive_damage(self, amount):
        self._life -= amount   # Se resta la vida
        print(f"{self.name} recibió {amount} de daño. Vida restante: {self._life}")
        return self._life


# OBJETOS DEL JUEGO
player = Character(500, 50, "Pepe")
enemy = Character(2000, 100, "Golem")

# Pociones
cura = Potion("Elixir", 2, "curativa", 350)
ira = Potion("Rabia", 1, "fortaleza", 1.5)


print("¡Bienvenido al juego!")
while True:
    opcion = int(input("Ingresa la opción:\n 1: Atacar\n 2: Mochila\n "))

    if opcion == 1:
        player.attack(enemy)

    elif opcion == 2:
        print("Mochila abierta")
        print("¿Qué deseas usar?\n 1: Poción de vida\n 2: Poción de fuerza\n")
        opcionpotion = int(input("Ingresa la opción: "))

        if opcionpotion == 1:
            cura.aplicar(player)   # Se aplica al jugador
        elif opcionpotion == 2:
            ira.aplicar(player)
        else:
            print("Opción inválida")
