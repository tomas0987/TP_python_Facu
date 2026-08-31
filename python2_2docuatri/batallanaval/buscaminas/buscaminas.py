class Tablero:
    
    def __init__(self,filas,columnas):
        self.filas=filas
        self.columnas=columnas
        self.celdas=[[celda() for i in range (columnas)]for i in range(filas)]

class Celda:
    
    def __init__(self,estado,haymina:bool,x,y):
        self.estado=estado
        self.haymina=haymina
        self.x=x
        self.y=y

n=int(input("ingrese un numero para la cantidad de filas: "))  
m=int(input("ingrese una cantidad de columnas: "))
tablerooculto=Tablero(n,m)            
celda=Celda("vacia",False,tablerooculto.columnas,tablerooculto.filas)            
      