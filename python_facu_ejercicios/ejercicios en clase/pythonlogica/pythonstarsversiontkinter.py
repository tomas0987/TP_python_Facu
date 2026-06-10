import random
import tkinter as tk
from PIL import Image, ImageTk

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
    def __init__(self, name, health, weapon, armor=None):
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
        else:
            self.health -= damage

        if self.health <= 0:
            self.health = 0
            print(f"{self.name} ha sido derrotado...")
        else:
            print(f"{self.name} tiene {int(self.health)} puntos de vida restantes.")

    def getCurrentHealth(self):
        return self.health


# ---------------- OBJETOS ----------------

pociones = Potion()
espada = Arma("Espada", 50, 100, 0.1, 2)
daga = Arma("Daga", 30, 60, 0.2, 1.5)
hacha = Arma("Hacha", 80, 90, 0, 0)

heroe = Character("Heroe", 5000, espada)
grandote = Character("Grandote", 2000, hacha)


# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("python Stars")
ventana.geometry("800x600")

bg_imagen = Image.open("C:/Users/sanch/Downloads/Copilot_20260609_172546.png")
bg_photo = ImageTk.PhotoImage(bg_imagen)

fondo = tk.Label(ventana, image=bg_photo)
fondo.image = bg_photo
fondo.place(x=0, y=0, relwidth=1, relheight=1)


# ----------------
# ---------------- FUNCIONES ----------------

def attack():
    heroe.attack(grandote)


def equipar_arma(arma):
    heroe._weapon = arma
    print(f"Has equipado: {arma.name}")


def open_mochila():
    mochila = tk.Toplevel(ventana)
    mochila.title("Mochila")
    mochila.geometry("300x350")
    mochila.config(bg="#2b2b2b")

    # --- BOTÓN POCIÓN DE VIDA ---
    btn_vida = tk.Button(
        mochila,
        text="Poción de Vida",
        width=20,
        height=2,
        command=lambda: pociones.health_potion(200)
    )
    btn_vida.pack(pady=10)

    # --- BOTÓN POCIÓN DE FUERZA ---
    btn_fuerza = tk.Button(
        mochila,
        text="Poción de Fuerza",
        width=20,
        height=2,
        command=lambda: pociones.strength_potion(3)
    )
    btn_fuerza.pack(pady=10)

    # --- BOTÓN EQUIPAR ESPADA ---
    btn_arma1 = tk.Button(
        mochila,
        text="Equipar Espada",
        width=20,
        height=2,
        command=lambda: equipar_arma(espada)
    )
    btn_arma1.pack(pady=10)

    # --- BOTÓN EQUIPAR HACHA ---
    btn_arma2 = tk.Button(
        mochila,
        text="Equipar Hacha",
        width=20,
        height=2,
        command=lambda: equipar_arma(hacha)
    )
    btn_arma2.pack(pady=10)


# ---------------- HUD ----------------

caja = tk.Frame(ventana, width=850, height=1000, bg="gray", highlightbackground="brown", highlightthickness=3)
caja.place(x=700, y=480)

btn_atack = tk.Button(caja, text="Atacar", width=19, height=7, command=attack)
btn_atack.place(x=600, y=1)

btn_mochila = tk.Button(caja, text="Mochila", width=19, height=7, command=open_mochila)
btn_mochila.place(x=400, y=1)


ventana.mainloop()