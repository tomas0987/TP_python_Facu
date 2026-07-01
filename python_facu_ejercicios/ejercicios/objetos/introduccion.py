class Persona:
    especie = "Humano"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"hola que tal, mi nombre es{self.nombre} y tengo {self.edad} anios de edad"
    
persona1 = Persona("Juan", 45)


