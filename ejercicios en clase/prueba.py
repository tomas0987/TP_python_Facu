
prueba = "zmor"
for i in range(len(prueba) - 1):
    primera = prueba[i]
    segunda = prueba[i + 1]
    print(primera, segunda)
    if primera > segunda:
        print('la palabra no esta ordenada alfabeticamente')
    else:
        print('la palabra esta ordenada alfabeticamente')
