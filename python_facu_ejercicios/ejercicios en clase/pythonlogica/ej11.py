palabra="neuquen"

def palindromo(palabra):
    if len(palabra) <= 1:      
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])
print(palindromo(palabra))