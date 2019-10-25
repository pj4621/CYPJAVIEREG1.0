serie = 0
n = int(input("Dame un numero entero: "))
for i in range(n,0,-1):
    serie = serie + (i**i)
print("El total acumulado es:",serie)
