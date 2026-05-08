
n= int(input("ingrese un numero: "))

def elmaestrofibo(n):
    if n ==0:
        return 0
    elif n==1 :
        return 1
    else:
        return elmaestrofibo(n-1) + elmaestrofibo(n-2)
      
print("el numero de fibonacci en la posicion ", n, "es: ", elmaestrofibo(n))    
