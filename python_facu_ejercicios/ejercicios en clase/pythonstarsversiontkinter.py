import random
import tkinter as tk
from PIL import Image, ImageTk

# ---------------- INTERFAZ PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("python Stars")
ventana.geometry("800x600")

bg_imagen = Image.open("C:/Users/sanch/Downloads/Copilot_20260609_172546.png")
bg_photo = ImageTk.PhotoImage(bg_imagen)

fondo = tk.Label(ventana, image=bg_photo)
fondo.image = bg_photo
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# HUD
caja = tk.Frame(ventana, width=850, height=1000, bg="gray", highlightbackground="brown", highlightthickness=3)
caja.place(x=700, y=480)

# Consola interna
consola = tk.Text(caja, width=35, height=30, bg="black", fg="white", font="Consolas")
consola.place(x=1, y=20)

def escribirConsola(texto):
    consola.insert(tk.END, texto + "\n")
    consola.see(tk.END)

# ---------------- EQUIPAMIENTO ----------------

class Arma:
    def __init__(self, name, minDamage, maxDamage, critChance, critMultiplier):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.critChance = critChance
        self.critMultiplier = critMultiplier

    def getDamage(self):
        return random.randint(self.minDamage, self.maxDamage)

class Armadura:
    def __init__(self, name, defense):
        self._name = name
        self._defense = defense

    def absorbDamage(self, damage):
        return max(damage - self._defense, 0)

# ---------------- POCIONES ----------------

class Potion:
    def health_potion(self, amount):
        if heroe.health >= heroe.maxHealth:
            escribirConsola("Salud al máximo, no se precisa curar.")
            return
        
        heroe.health = min(heroe.health + amount, heroe.maxHealth)
        escribirConsola(f"Te has curado. HP actual: {heroe.health}")
    
    def strength_potion(self, duration):
        escribirConsola(f"Poción de fuerza consumida. Aumentando daño por {duration} turnos.")

# ---------------- PERSONAJE ----------------

class Character:
    def __init__(self, name, health, weapon, armor=None):
        self.name = name
        self.maxHealth = health
        self.health = health
        self._weapon = weapon
        self._armor = armor

    def attack(self, target):
        realDamage = self._weapon.getDamage() * random.uniform(0.9, 1.15)

        if random.random() < self._weapon.critChance:
            realDamage *= self._weapon.critMultiplier
            escribirConsola("¡Golpe crítico!")

        escribirConsola(f"{self.name} atacó a {target.name} causando {int(realDamage)} de daño.")
        target.receiveDamage(realDamage)
    
    def receiveDamage(self, damage):
        if self._armor:
            damage -= self._armor.absorbDamage(damage)

        self.health -= damage

        if self.health <= 0:
            self.health = 0
            escribirConsola(f"{self.name} ha sido derrotado...")
        else:
            escribirConsola(f"{self.name} tiene {int(self.health)} puntos de vida restantes.")

# ---------------- OBJETOS ----------------

pociones = Potion()
espada = Arma("Espada", 50, 100, 0.1, 2)
daga = Arma("Daga", 30, 60, 0.2, 1.5)
hacha = Arma("Hacha", 80, 90, 0, 0)

# ---------------- INPUT DE VIDA DESDE TKINTER ----------------

def pedirVidaHeroe():
    
    # Frame interno dentro de la ventana principal
    frame_vida = tk.Frame(ventana, bg="#222", bd=3, relief="ridge")
    frame_vida.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame_vida, text="Vida inicial del héroe:", fg="white", bg="#222",
             font=("Consolas", 12)).pack(pady=10)

    entrada = tk.Entry(frame_vida, font=("Consolas", 12))
    entrada.pack(pady=5)

    def confirmar():
        try:
            vida = int(entrada.get())

            if vida <= 0:
                raise ValueError
        except ValueError:
            vida = 500
            escribirConsola("Valor inválido, se asigna 500.")

        global heroe
        heroe = Character("Heroe", vida, espada)

        frame_vida.destroy()  # desaparece el panel

    tk.Button(frame_vida, text="Aceptar", font=("Consolas", 12),
              command=confirmar).pack(pady=10)


pedirVidaHeroe()

grandote = Character("Grandote", 2000, hacha)

# ---------------- FUNCIONES ----------------

def attack():
    # Turno del héroe
    heroe.attack(grandote)

    # Turno del enemigo con delay
    if grandote.health > 0:
        ventana.after(800, lambda: grandote.attack(heroe))

def equipar_arma(arma):
    heroe._weapon = arma
    escribirConsola(f"Has equipado: {arma.name}")

def open_mochila():
    mochila = tk.Toplevel(ventana)
    mochila.title("Mochila")
    mochila.geometry("300x350")
    mochila.config(bg="#2b2b2b")

    tk.Button(mochila, text="Poción de Vida", width=20, height=2,
              command=lambda: pociones.health_potion(200)).pack(pady=10)

    tk.Button(mochila, text="Poción de Fuerza", width=20, height=2,
              command=lambda: pociones.strength_potion(3)).pack(pady=10)

    tk.Button(mochila, text="Equipar Espada", width=20, height=2,
              command=lambda: equipar_arma(espada)).pack(pady=10)

    tk.Button(mochila, text="Equipar Hacha", width=20, height=2,
              command=lambda: equipar_arma(hacha)).pack(pady=10)

# ---------------- BOTONES ----------------

btn_atack = tk.Button(caja, text="Atacar", width=19, height=7, command=attack)
btn_atack.place(x=600, y=1)

btn_mochila = tk.Button(caja, text="Mochila", width=19, height=7, command=open_mochila)
btn_mochila.place(x=400, y=1)

ventana.mainloop()
