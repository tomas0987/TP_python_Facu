import random
import tkinter as tk
from PIL import Image, ImageTk

# ---------------- INTERFAZ PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("python Stars")

# Cargar fondo 
bg_imagen = Image.open("imagenes/fondo.png")   
ancho, alto = bg_imagen.size
bg_photo = ImageTk.PhotoImage(bg_imagen)

# Ajustar ventana al tamaño real del fondo
ventana.geometry(f"{ancho}x{alto}")

# Canvas para permitir transparencia
canvas = tk.Canvas(ventana, width=ancho, height=alto, highlightthickness=0)
canvas.place(x=0, y=0)

# Dibujar fondo en el canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ---------------- SPRITES ----------------

img_heroe = Image.open("imagenes/heroe.png")   
img_heroe = img_heroe.resize((250, 220), Image.NEAREST)
heroe_photo = ImageTk.PhotoImage(img_heroe)
canvas.create_image(170, 390, image=heroe_photo, anchor="nw")

img_grandote = Image.open("imagenes/grandote.png")   
img_grandote = img_grandote.resize((250, 250), Image.NEAREST)
grandote_photo = ImageTk.PhotoImage(img_grandote)
canvas.create_image(900, 140, image=grandote_photo, anchor="nw")

# ---------------- BARRAS DE VIDA ----------------

barra_heroe = tk.Canvas(ventana, width=250, height=20, bg="red", highlightthickness=0)
barra_heroe.place(x=150, y=320)

barra_grandote = tk.Canvas(ventana, width=250, height=20, bg="red", highlightthickness=0)
barra_grandote.place(x=900, y=90)

def actualizar_barras():
    if 'heroe' in globals():
        porcentaje = heroe.health / heroe.maxHealth
        barra_heroe.config(width=max(1, int(250 * porcentaje)))
    if 'grandote' in globals():
        porcentaje2 = grandote.health / grandote.maxHealth
        barra_grandote.config(width=max(1, int(250 * porcentaje2)))

# ---------------- HUD ----------------

caja = tk.Frame(ventana, width=850, height=1000, bg="#333",
                highlightbackground="gold", highlightthickness=4)
caja.place(x=700, y=480)

# Scrollbar
scroll = tk.Scrollbar(caja)
scroll.place(x=350, y=20, height=480)

# Consola con scroll
consola = tk.Text(
    caja,
    width=35,
    height=30,
    bg="black",
    fg="white",
    font="Consolas",
    yscrollcommand=scroll.set
)
consola.place(x=1, y=20)

scroll.config(command=consola.yview)


# ---------------- CONSOLA FLUIDA (OPCIÓN 2 OPTIMIZADA) ----------------

cola_mensajes = []
escribiendo = False

def escribirConsola(texto, velocidad=5):
    cola_mensajes.append((texto, velocidad))
    if not escribiendo:
        procesar_cola()

def procesar_cola():
    global escribiendo

    if not cola_mensajes:
        escribiendo = False
        return

    escribiendo = True
    texto, velocidad = cola_mensajes.pop(0)

    def escribir_lento(i=0):
        if i < len(texto):
            consola.insert(tk.END, texto[i])
            consola.see(tk.END)
            ventana.after(velocidad, lambda: escribir_lento(i+1))
        else:
            consola.insert(tk.END, "\n")
            consola.see(tk.END)
            ventana.after(50, procesar_cola)

    escribir_lento()

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
        escribirConsola(f"Te has curado. HP actual: {int(heroe.health)}")
        actualizar_barras()
    
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
            damage = self._armor.absorbDamage(damage)

        self.health -= damage

        if self.health < 0:
            self.health = 0

        escribirConsola(f"{self.name} tiene {int(self.health)} puntos de vida restantes.")
        actualizar_barras()

        if self.health <= 0:
            escribirConsola(f"{self.name} ha sido derrotado...")

            if self.name == "Heroe":
                ventana.after(500, lambda: mostrar_resultado("Perdiste"))
            else:
                ventana.after(500, lambda: mostrar_resultado("¡Ganaste!"))

# ---------------- RESULTADO ----------------

def mostrar_resultado(resultado):
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("300x200")
    ventana_resultado.config(bg="#222")

    tk.Label(
        ventana_resultado,
        text=resultado,
        font=("Consolas", 18, "bold"),
        fg="white",
        bg="#222"
    ).pack(pady=20)

    def reiniciar():
        ventana_resultado.destroy()
        reiniciar_juego()

    tk.Button(
        ventana_resultado,
        text="Reiniciar",
        font=("Consolas", 14),
        width=12,
        command=reiniciar
    ).pack(pady=5)

    tk.Button(
        ventana_resultado,
        text="Salir",
        font=("Consolas", 14),
        width=12,
        command=ventana.quit
    ).pack(pady=5)

def reiniciar_juego():
    global heroe, grandote

    consola.delete("1.0", tk.END)

    heroe = Character("Heroe", heroe.maxHealth, espada)
    grandote = Character("Grandote", 2000, hacha)

    actualizar_barras()
    escribirConsola("¡Nueva partida iniciada!")

# ---------------- OBJETOS ----------------

pociones = Potion()
espada = Arma("Espada", 50, 100, 0.1, 2)
hacha = Arma("Hacha", 80, 90, 0, 0)
armadura_heroica = Armadura("Armadura Heroica", 35)

# ---------------- INPUT DE VIDA ----------------

def pedirVidaHeroe():
    frame_vida = tk.Frame(ventana, bg="#222", bd=3, relief="ridge")
    frame_vida.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame_vida, text="Vida inicial del héroe:",
             fg="white", bg="#222", font=("Consolas", 12)).pack(pady=10)

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
        heroe = Character("Heroe", vida, espada, None)

        frame_vida.destroy()
        actualizar_barras()

    tk.Button(frame_vida, text="Aceptar", font=("Consolas", 12),
              command=confirmar).pack(pady=10)

pedirVidaHeroe()

grandote = Character("Grandote", 2000, hacha, None)
actualizar_barras()

# ---------------- FUNCIONES ----------------

def attack():
    heroe.attack(grandote)
    if grandote.health > 0:
        ventana.after(800, lambda: grandote.attack(heroe))

def equipar_arma(arma):
    heroe._weapon = arma
    escribirConsola(f"Has equipado: {arma.name}")

def equipar_armadura(armadura):
    if heroe._armor is None:
        heroe._armor = armadura
        escribirConsola(f"Has equipado: {armadura._name}")
    else:
        heroe._armor = None
        escribirConsola("Has quitado la armadura. Ahora recibes daño completo.")

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

    tk.Button(mochila, text="Equipar Armadura", width=20, height=2,
              command=lambda: equipar_armadura(armadura_heroica)).pack(pady=10)

# ---------------- BOTONES ----------------

estilo_boton = {
    "bg": "#444",
    "fg": "white",
    "activebackground": "#666",
    "activeforeground": "white",
    "font": ("Consolas", 12, "bold"),
    "bd": 3,
    "relief": "ridge"
}

btn_atack = tk.Button(caja, text="⚔ Atacar", width=19, height=7,
                      command=attack, **estilo_boton)
btn_atack.place(x=600, y=1)

btn_mochila = tk.Button(caja, text="🎒 Mochila", width=19, height=7,
                        command=open_mochila, **estilo_boton)
btn_mochila.place(x=400, y=1)

ventana.mainloop()
