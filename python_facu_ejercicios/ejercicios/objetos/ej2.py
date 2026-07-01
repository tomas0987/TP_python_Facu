class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        area = self.base * self.altura
        print(f"area del rectangulo: {area}")
        
    def calcular_perimetro(self):
        perimetro = (self.base + self.altura) * 2
        print(f"el perimetro es: {perimetro}")
        
base = int(input("ingresar ancho del rectangulo"))
altura = int(input("ingresar alto del rectangulo"))

rec1 = Rectangulo(base, altura)

rec1.calcular_area()
rec1.calcular_perimetro()