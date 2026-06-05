class persona:
    def atributos_persona(self,nombre,apellido,anios):
        self.nombre=nombre
        self.apellido=apellido
        self.anios=anios
    def saludar(self):
        print(f"hola buenas{nombre} {apellido}, usted tiene {anios} anios de edad")

nombre=input("ingresa el nombre de la persona")
apellido=input("ingresa el apellido de la persona")
anios=input("ingresa la edad de la persona")

p=persona()

p.atributos_persona(nombre,apellido,anios)
p.saludar()