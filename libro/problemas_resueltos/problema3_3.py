serie = 0
n = int(input("Dame un numero entero: "))
band = 't'
for i in range(n,0,-1):
    if band == 't':
        serie += 1/i
        band = 'f'
    else:
        serie += -1/i
        band = 't'
print("la serie es",serie)

