n=0
contactos=[]
numero=[]
while n==0:
    nom=input("ingrese el nombre del contacto:").capitalize()
    print(f"el nombre ingresado es:{nom}")
    num=int(input("ingrese el nuumero de telefono:"))
    print(f"el numero ingresado es:{num}")
    contactos.append(nom)
    numero.append(num)
    condicion=input('desea ingresar otro contacto?').lower()
    if condicion=="no":
        break


with open("contactos.txt","a",encoding="utf-8") as archivo:
    for i in range(len(contactos)):
        archivo.write(f"nombre:{contactos[i]}, telefono:{numero[i]}\n")
