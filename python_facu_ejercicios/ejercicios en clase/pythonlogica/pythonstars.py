class potion:
    def life_potion(self,cantlife):
      self.cantlife=cantlife
      p.life+=self.cantlife
      if p.life==500:
          print("salud al maximo no se precisa de curar")
      else:
          print("te has curado")
          print("vida actual{p.currenhealth}")














class character:
    def __init__(self, name, _life,_currenthealth,damage, critChance):
        self.name = name
        self.life = life
        self.damage = damage
        self._currenthealth=_currenthealth

    def attack(self, target):
        damage = self.damage
        target.receiveDamage(damage)

        
    
    def receiveDamage(self, damage):
        self.life -= damage
        if self.life <= 0:
            print(f"{self.name} has been defeated.")
            duendecito= character("duende",200,10,0.666,0.333)
        else:
            print(f"{self.name} has {self.life} life remaining.")
    def currenthealth(self):
        return self._currenthealth
    
    




print("welcome to the best game of the universe!!!!!!!!!")
p=character("chiquito",500,50,25)


while True:
    pass