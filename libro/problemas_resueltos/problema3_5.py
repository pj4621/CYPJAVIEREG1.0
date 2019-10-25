sumotr = 0
sumpos= 0
cuepos = 0
n = int(input("Dame un numero entero: "))
for i in range(n,0,-1):
    num = float(input("Ingresa un valor numerico: "))
    if num > 0:
        sumpos += num
        cuepos += 1
    else:
        sumotr += num
progen = (sumpos+sumotr)/n
propos = (sumpos/cuepos)
print("El total de numeros positivos ingresados es:",cuepos)
print("El promedio de los numeros positivos es igual a:",propos)
print("El promedio general de los numeros es:",progen)

    


