import random, shutil, time

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
            print(f"{self.name} tiene {self.life} puntos de vida.")
    
    def getCurrentHealth(self):
        return self._currentHealth

# "Interfaz" profesional
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

heroe = character("Heroe",500,500,50,0.1,2)

grandote = character("Grandote", 2000, 2000, 75, 0, 0)

if grandote.getCurrentHealth() <= 0: # Arreglar -----------------------------------------------------------------------------------------------------
    time.sleep(1) # Es para agregar suspenso al juego, completamente necesario
    print("Grandecito llevaba consigo un duende!")
    duendecito = character("duende",200, 200, 30, 0.666, 1.5)

while True:
    pass
