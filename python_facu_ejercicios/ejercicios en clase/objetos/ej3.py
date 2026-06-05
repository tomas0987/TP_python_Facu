class estudiante:
    def alumno(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def promedio(self):
        self.prom = (self.nota1 + self.nota2 + self.nota3) / 3
        return self.prom
    def aprobado(self):
        self.aprob = self.prom >= 6
        return self.aprob

nombre = input("ingresa el nombre del alumno")
nota1 = int(input("ingrese la primer nota"))
nota2 = int(input("ingrese la segunda nota"))
nota3 = int(input("ingrese la tercer nota"))

c = estudiante()
c.alumno(nombre, nota1, nota2, nota3)
prom = c.promedio()
aprob = c.aprobado()
print(f"Promedio: {prom}")
print(f"Aprobado: {aprob}")
