class electico:
    def __init__(self, estado, velocidad):
        self.estado = estado
        self.velocidad = velocidad

    def cambiar_estado(self):
        print("si desea prender ingrese 'on', si desea apagar 'off'")
        self.cambio = input("off/on:").lower()
        if self.cambio == "off":
            self.estado = False
            self.velocidad=0
        elif self.cambio == "on":
            self.estado = True
            self.velocidad=1
        else:
            print("Entrada no válida")
        
    def cambiar_velocidad(self):
        self.var=int(input("ingresa la velocidad a la que desea cambiar(0,1,2,3)"))
        if self.var==0:
            self.estado=False
        elif self.var==1:
            self.velocidad=1
        elif self.var==2:
            self.velocidad=2
        elif self.var==3:
            self.velocidad=3
p=electico(False,0)

while True:
    print("ingrese que desea hacer: 1:cambiar estado. 2:cambiar velocidad")
    r=int(input("ingrese la opcion 1 o 2:"))
    if r==1:
        p.cambiar_estado()
        print(f"el estado actual es:{p.estado} y la velocidad es:{p.velocidad}")
    elif r==2:
        p.cambiar_velocidad()
        print(f"el estado actual es:{p.estado} y la velocidad es:{p.velocidad}")
    else:
        print("opcion invalidad")
          