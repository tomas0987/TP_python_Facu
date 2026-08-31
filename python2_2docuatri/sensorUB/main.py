import sensor,random

def main():
    sensormonitoreo= sensor.SensorTermico("A1","Rack: A-4",[])
    while True:
        print("Bienven1do")
        print("""Ingrese la opcion que desea elegir: \n
              1-actualizar sensores\n
              2-sacar maximo\n
              3-sacar promedio\n
              4-mostrar listado""")
        try:
            opcion=int(input("ingrese la opcion: "))
            match opcion:
                case 1:
                    temp= random.randint(0,90)
                    if sensormonitoreo.agregar_lectura(temp):
                        print(f'lectura agrgegada: {temp}')
                    else:
                        print(f'fuera de rango')
            
                case 3:
                    try:
                        print(f' el promedio es: {sensormonitoreo.obtener_promedio()}')
                    except ValueError as e:
                        print(e)
                
                case 4:
                    print(f'Listado: {sensormonitoreo.temperaturas}')
                
                case 2:
                    print(f"maximo: {sensormonitoreo.obtener_maxima()}")
        except ValueError:
            print("el numero ingresado no corresponde a una accion")    
    
    
    
    
    
    




if __name__ == "__main__":
    main()
    