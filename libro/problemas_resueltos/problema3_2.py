band = 'T'
sumser = 0
I = 2
while I <= 18:
    sumser += +1
    print(I)
    if band == 'T':
        band = 'F'
        I = 1 + 3
    else:
        band = 'T'
        I = 1 + 2
print(sumser)
