band = 'T'
sumser = 0
I = 2
while I <= 1800:
    sumser += 1
    print("El incremento es:",I)
    if band == 'T':
        band = 'F'
        I += 3
    else:
        band = 'T'
        I += 2
print("los terminos de la serie son:",sumser)
