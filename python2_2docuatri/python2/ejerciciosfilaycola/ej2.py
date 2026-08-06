lista=[]
contador1=0
contador2=0
def verificador(lista,contador1,contador2):
    for n in lista[0::2]:
        if n=="(":
            contador1+=1
    for m in lista[1::2]:
        if m==")":
            contador2+=1
    return contador1,contador2

texto= input("ingrese un texto con parentesis:")
for i in texto:
    if i== "(" or i == ")":
        lista.append(i)

contador1,contador2=verificador(lista,contador1,contador2)
print(lista)
print(contador1,contador2)
if contador1==contador2:
    print("los parentesis estan correctos")
else:
    print("los parentesis estan mal")
    
            


