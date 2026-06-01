with open("frases.txt","r",encoding="utf-8")as archivo:
   num=0
   contador_lineas=0
   contador_palabras=0
   contador_letras=0
   while num==0:
       
    linea= archivo.readline()
    contador_lineas+=1
    
    if linea=="":
        contador_lineas=contador_lineas-1
        break
   
print(f"la cantidad de lineas que tiene el archivo son:{contador_lineas}") 
with open("frases.txt","r",encoding="utf-8")as archivo:
    contenido=(archivo.read())
    a=contenido.replace("\n"," ")
    print(a)
    b= a.replace(" ","")
    print(b)
    for i in b:
        contador_letras+=1
print (f"el total de plabras que tiene el texto es: {contador_letras}")
      

        