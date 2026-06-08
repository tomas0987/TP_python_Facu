import random, shutil, time
class equipment:
    def HeroicSword(self, equip):
        self.equip = equip
        if equip == True:
            heroe.damage *= 1.5
            print("te has equipado la espada heroica tu danio aumento un 50%")
            
        

class potion:
    def health_potion(self, amount):
      self.amount = amount
      heroe.health += self.amount
      if heroe.life == 500:
          print("Salud al maximo no se precisa de curar")
      else:
          print("Te has curado")
          print(f"HP: {p.currenhealth}")

class character:
    def __init__(self, name, health, _currentHealth, damage, critChance, critMultiplier):
        self.name = name
        self.health = health
        self._currentHealth= _currentHealth
        self.damage = damage
        self.critChance = critChance
        self.critMultiplier = critMultiplier

    def attack(self, target):
        realDamage = self.damage * random.uniform(0.9, 1.15)

        target.receiveDamage(realDamage)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"Has matado a {self.name}...")
        else:
            print(f"{self.name} tiene {self.health} puntos de vida.")
    
    def getCurrentHealth(self):
        return self._currentHealth

# "Interfaz" profesional1
width = shutil.get_terminal_size().columns # Para centrar el titulo

# Darle color al logo 31m: rojo, 37m: blanco

logo="""                                
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

creditos ="""
\033[30m       Built by:     \033[0m
\033[30m    Tomas Sanchez    \033[0m
\033[30m     Franco Leone    \033[0m
"""

print("\033[30mPor: Tomas Sanchez y Franco Leone\033[0m".center(width))
equipo=equipment()
heroe = character("Heroe",500,500,50,0.1,2)

grandote = character("Grandote", 2000, 2000, 75, 0, 0)

if grandote.getCurrentHealth() <= 0: # Arreglar -----------------------------------------------------------------------------------------------------
    time.sleep(1) # Es para agregar suspenso al juego, completamente necesario
    print("Grandecito llevaba consigo un duende!")
    duendecito = character("duende",200, 200, 30, 0.666, 1.5)

while True:
    option=int(input("elige lo que desea hacer el heroe:\n 1: atacar\n 2: abrir mochila"))
    if option==1:
        heroe.attack(grandote)
    elif option==2:
        while True:
            optionBag=int(input("mochila abierta que desea hacer?\n 1: Abrir bolsa de pociones\n 2: armamento"))
            if optionBag==1:
                potion.health_potion(heroe)
            elif optionBag==2:
                confirmoespada=input("solo posees una espada, deseas equiparla?").lower()
                if confirmoespada=="si":
                    equipo.HeroicSword(True)
                    break
                
    
