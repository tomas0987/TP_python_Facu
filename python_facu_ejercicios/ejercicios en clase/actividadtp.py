#---------------ej 1----------------


n=int(input("ingrese un numero para calcular el factorial"))
def factorial(n):
    if n==0:
        return 1
    
    else:
        return n*factorial(n-1)
print(f"el factorial de {n} es {factorial(n)}")

#----------------ej2--------------------


n= int(input("ingrese un numero: "))

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
print("la suma de los numeros hasta ", n, "es: ", suma(n))



#---------------ej3----------------------
def contador(n):
    if n == 0:
        return
    else:
        contador(n - 1)   # Llamada recursiva primero
        print(n)          # Se imprime al "volver" de la recursión

n = int(input("Ingrese un número: "))
print("Los números desde 1 hasta", n, "son:")
contador(n)

#---------------------------ej4------------------
n= int (input("ingrese un numero: "))

def contador(n):
    if n == 0 :
        return 0
    else:
        print(n)
        return contador(n-1)
print("los numeros hasta ", n, "son: ")
contador(n)
#-------------------------ej5-------------------
def potencia(a,b):
    if b ==0:
        return 1
    else:
        return a* potencia(a,b-1)
a= int(input("ingrese la base: "))
b= int(input("ingrese el exponente: "))
print("el resultado de ", a, "elevado a ", b, "es: ", potencia(a,b))
#--------------------------ej6---------------------
lista=[1,2,3,4,5]
def sumaValores(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+sumaValores(lista[1:])
print(f"los valores son: {sumaValores(lista)}")   

#------------------------ej7----------------
from operator import index

lista=["pelota","milanesa","programacion","plumas"]

def contarElementos(lista):
    if not lista:
        return 0
    else:
        return 1 + contarElementos(lista[1:])
print(contarElementos(lista))
#--------------------ej8--------------------

lista=[1,2,3,4,5]
i=0
def maxnum(lista,i):
    if lista[i]>=(lista[i+1]):
        return lista[i]
    
    else:
        i+=1
        return (maxnum(lista[i]))
print(maxnum(lista,i))





#--------------------ej9---------------
lista=[1,2,3,4,5]
def invertirLista(lista):
    if len(lista)<=1:
        return lista
    else:
        return invertirLista(lista[1:])+[lista[0]]
print(invertirLista(lista))
#-----------------------ej10---------------------
num=12345

def sumadigitos(num):
    suma = 0
    for i in str(num):
        suma += int(i)
    return suma

print(sumadigitos(num))
#------------------ej11-----------
palabra="neuquen"

def palindromo(palabra):
    if len(palabra) <= 1:      
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])
print(palindromo(palabra))
#------------------ej12----------------

n= int(input("ingrese un numero: "))

def elmaestrofibo(n):
    if n ==0:
        return 0
    elif n==1 :
        return 1
    else:
        return elmaestrofibo(n-1) + elmaestrofibo(n-2)
      
print("el numero de fibonacci en la posicion ", n, "es: ", elmaestrofibo(n))    
#---------------------------ej13-----------------------
palabra=list("argentina")
def contarelementos(palabra):
    if palabra == []:          
        return 0
    else:
        return 1 + contarelementos(palabra[1:])

print(contarelementos(palabra))
#----------------------------ej14----------------------



def conversionbinario(n):
    if n ==0:
        return "0"
    elif n ==1:
        return "1"
    else:
        return conversionbinario(n//2)+ str(n%2)

print(conversionbinario(3))

#------------------ej15-----------------
lista=[1,2,3]
def productelement(lista):
    if lista==[]:
        return 1
    else:
        return lista[0]* productelement(lista[1:])
print(productelement(lista))
#---------------------ej16-------------------
lista=[1,2,3,4,2,2]
def eliminar(lista,x):
    if lista==[]:
        return []
    elif lista[0]== x:
        return eliminar(lista[1:],x)
    else:
        return[lista[0]]+eliminar(lista[1:],x)
print(eliminar(lista,2))

#-----------------------ej17-------------------
lista=[1,2,3,4,5]
def orden(lista):
    if lista==[]:
        return True
    elif len(lista)==1:
        return True
    elif lista[0]>lista[1]:
        return False
    return orden (lista[1:])
print(orden(lista))
#------------------ej18--------------
lista=[1,2,[1,[45]]]

def profundidad(lista):
    if  not isinstance(lista,list):
        return 0
    if lista==[]:
        return 1
    else:
        return 1 + max(profundidad(i)for i in lista)
print(profundidad(lista))
#--------------------ej19-------------------
lista = [1, [2, 3]]

def suma(lista):
    sumaTotal = 0
    for elem in lista:
        if isinstance(elem, list):
            sumaTotal += suma(elem)
        else:
            sumaTotal += elem
    return sumaTotal

print(suma(lista))
#---------------------------ej20---------------

