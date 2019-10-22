sumpar = 0
sumimp = 0
cuepar = 0
for i in range (1,10,1):
    num = float(input("Ingresa un numero entero: "))
    if num < 0 and num > 0 :
        if ((-1) ** num) > 0: 
            cuepar += 1
            sumpar += num
            
        else:
            sumimp += num
propar = sumpar / cuepar 
print(f"es {propar} y {sumimp}")

