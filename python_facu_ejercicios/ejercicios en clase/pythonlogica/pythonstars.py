import random, shutil, time
import tkinter as tk



# ---------------- EQUIPAMIENTO ----------------

class Arma:
    def __init__(self, name, minDamage, maxDamage, critChance, critMultiplier):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.critChance = critChance
        self.critMultiplier = critMultiplier

    def __str__(self):
        return f"{self.name} (Daño: {self.minDamage} - {self.maxDamage})"

    def getDamage(self):
        return random.randint(self.minDamage, self.maxDamage)

class Armadura:
    def __init__(self, name, defense):
        self._name = name
        self._defense = defense

    def absorbDamage(self, damage):
        reducedDamage = damage - self._defense
        return max(reducedDamage, 0)
    
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
    
    def strength_potion(self, duration):
        print(f"Poción de fuerza consumida. Aumentando daño por {duration} turnos.")


# ---------------- PERSONAJE ----------------

class Character:
    def __init__(self, name, health, weapon, armor = None):
        self.name = name
        self.maxHealth = health
        self.health = health
        self._weapon = weapon
        self._armor = armor

    def __str__(self):
        return f"{self.name} (HP: {int(self.health)} / {self.maxHealth} - Arma: {self._weapon})"

    def attack(self, target):
        realDamage = self._weapon.getDamage() * random.uniform(0.9, 1.15)

        # crítico
        if random.random() < self._weapon.critChance:
            realDamage *= self._weapon.critMultiplier
            print("¡Golpe crítico!")

        print(f"{self.name} atacó a {target.name} causando {int(realDamage)} de daño.")
        target.receiveDamage(realDamage)
    
    def receiveDamage(self, damage):
        
        if self._armor is not None:
            self.health -= damage - self._armor.absorbDamage(damage)
            print(f"{self.name} absorbió {int(damage - self.health)} de daño")
        else:
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

pociones = Potion()

try:
    vida = int(input("Ingrese cuanta vida quiere que su heroe tenga: "))
except ValueError:
    print("Valor no válido, se asignará la vida por defecto (500).")
    vida = 500

espada = Arma("Espada", 50, 100, 0.1, 2)
daga = Arma("Daga", 30, 60, 0.2, 1.5)
hacha = Arma("Hacha", 80, 90, 0, 0)

heroe = Character("Heroe", vida, espada)
grandote = Character("Grandote", 2000, hacha)

# ---------------- LOOP PRINCIPAL ----------------

while True:
    try:
        option = int(input("\nElige lo que desea hacer el héroe:\n 1: Atacar\n 2: Abrir mochila\n> "))
    except ValueError:
        print("Valor no válido.")
        continue

    match option:
        case 1:
            heroe.attack(grandote)

            if grandote.health <= 0:
                print("¡Has derrotado al Grandote!")
                break

            time.sleep(3)

            # Turno del enemigo
            print("\n--- Turno del enemigo ---")
            grandote.attack(heroe)

            if heroe.health <= 0:
                print("Has muerto...")
                break

            time.sleep(3)
        
        case 2:
            while True:
                try:
                    optionBag = int(input("\nMochila abierta. ¿Qué desea hacer?\n 1: Poción de vida\n 2: Poción de fuerza\n 3: Alternar arma \n 5: Volver\n> "))
                except ValueError:
                    print("Valor no válido.")
                    continue

                match optionBag:
                    case 1:
                        pociones.health_potion(200)
                    case 2:
                        pociones.strength_potion(3)
                    case 3:
                        if heroe._weapon == espada:
                            heroe._weapon = daga
                            print("Has equipado la Daga.")
                        elif heroe._weapon == daga:
                            heroe._weapon = espada
                            print("Has equipado la espada.")
                    case 4:
                        break

                if optionBag == 1:
                    pociones.health_potion(200)

                elif optionBag == 2:
                    confirmoespada = input("Solo posees una espada. ¿Deseas equiparla? (si/no): ").lower()
                    
                    if confirmoespada == "si":
                        heroe._weapon = espada
                        break

                elif optionBag == 5:
                    break
        case _:
            print("Opción no válida.")

#creacion de ventana 

