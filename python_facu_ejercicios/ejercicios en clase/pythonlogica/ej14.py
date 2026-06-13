def conversionbinario(n):
    if n ==0:
        return "0"
    elif n ==1:
        return "1"
    else:
        return conversionbinario(n//2)+ str(n%2)

print(conversionbinario(3))
