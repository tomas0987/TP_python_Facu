import random, shutil, time

# ---------------- EQUIPAMIENTO ----------------

class Equipment:
    def HeroicSword(self, equip):
        if equip:
            heroe.damage *= 1.5
            print("Te has equipado la espada heroica. Tu daño aumentó un 50%.")


# ---------------- POCIONES ----------------

class Potion:
    def health_potion(self, amount):
        if heroe.health >= heroe.maxHealth:
            print("Salud al máximo, no se precisa curar.")
            return
        
        heroe.health += amount
        if heroe.health > heroe.maxHealth:
            heroe.health = heroe.maxHealth
        
        print(f"Te has curado. HP actual: {heroe.health}")


# ---------------- PERSONAJE ----------------

class Character:
    def __init__(self, name, health, damage, critChance, critMultiplier):
        self.name = name
        self.maxHealth = health
        self.health = health
        self.damage = damage
        self.critChance = critChance
        self.critMultiplier = critMultiplier

    def attack(self, target):
        realDamage = self.damage * random.uniform(0.9, 1.15)

        # crítico
        if random.random() < self.critChance:
            realDamage *= self.critMultiplier
            print("¡Golpe crítico!")

        print(f"{self.name} atacó a {target.name} causando {int(realDamage)} de daño.")
        target.receiveDamage(realDamage)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} ha sido derrotado...")
        else:
            print(f"{self.name} tiene {int(self.health)} puntos de vida restantes.")

    def getCurrentHealth(self):
        return self.health


# ---------------- INTERFAZ ----------------

width = shutil.get_terminal_size().columns

logo = """                                
\033[31m                   ▄▄                \033[0m
\033[31m              ██   ██                \033[0m
\033[31m ████▄ ██ ██ ▀██▀▀ ████▄ ▄███▄ ████▄ \033[0m
\033[31m ██ ██ ██▄██  ██   ██ ██ ██ ██ ██ ██ \033[0m
\033[31m ████▀  ▀██▀  ██   ██ ██ ▀███▀ ██ ██ \033[0m
\033[31m ██      ██                          \033[0m
\033[31m ▀▀    ▀▀▀                           \033[0m
\033[37m            ██                       \033[0m
\033[37m     ▄█▀▀▀ ▀██▀▀ ▀▀█▄ ████▄ ▄█▀▀▀    \033[0m
\033[37m     ▀███▄  ██  ▄█▀██ ██ ▀▀ ▀███▄    \033[0m
\033[37m     ▄▄▄█▀  ██  ▀█▄██ ██    ▄▄▄█▀    \033[0m
"""

for line in logo.split("\n"):
    print(line.center(width))

print("\033[30mPor: Tomas Sanchez y Franco Leone\033[0m".center(width))


# ---------------- OBJETOS DEL JUEGO ----------------

equipo = Equipment()
pociones = Potion()

heroe = Character("Heroe", 500, 50, 0.1, 2)
grandote = Character("Grandote", 2000, 75, 0, 0)


# ---------------- LOOP PRINCIPAL ----------------

while True:
    option = int(input("\nElige lo que desea hacer el héroe:\n 1: Atacar\n 2: Abrir mochila\n> "))

    if option == 1:
        heroe.attack(grandote)

        if grandote.health <= 0:
            print("¡Has derrotado al Grandote!")
            break

        # Turno del enemigo
        print("\n--- Turno del enemigo ---")
        grandote.attack(heroe)

        if heroe.health <= 0:
            print("Has muerto...")
            break

    elif option == 2:
        while True:
            optionBag = int(input("\nMochila abierta. ¿Qué desea hacer?\n 1: Poción de vida\n 2: Equipar espada\n 3: Volver\n> "))

            if optionBag == 1:
                pociones.health_potion(200)

            elif optionBag == 2:
                confirmoespada = input("Solo posees una espada. ¿Deseas equiparla? (si/no): ").lower()
                if confirmoespada == "si":
                    equipo.HeroicSword(True)
                break

            elif optionBag == 3:
                break
